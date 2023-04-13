from flask import Flask, render_template, request
import sys
import mysql.connector


app = Flask(__name__)



def get_db():
   db = mysql.connector.connect(
      host="mysql_container",
      user="root",
      password="root",
      database="db_project_CloudComputing"
   )  
   return db

@app.route('/store', methods=['GET','POST'])
def store():
   data = request.get_json()
   print(format(data), file=sys.stderr)

   db = get_db()
   sql = """INSERT INTO TrafficData(SensorName,CarType, Speed, Date_Time) VALUES(%s,%s,%s,%s);"""
   cur = db.cursor()
   cur.execute(sql, (data["sensorName"],data["type"], data["speed"], data["date"]))
   db.commit()
   
   return "hello"

@app.route('/getAllData', methods=['GET'])
def getData():

   db = get_db()
   sql = "SELECT * FROM TrafficData;"
   cur = db.cursor()
   cur.execute(sql)
   result = cur.fetchall()
   data = []
   for x in result:
        car = {
            "sensorName": x[4],
            "carType":x[1],
            "speed": x[2],
            "type":x[3]
        }
        data.append(car)

   maxSpeed = getMaxSpeed(db)
   minSpeed = getMinSpeed(db)
   avgSpeed = getAvgSpeed(db)

   return render_template('home.html', result = result, data= data, maxSpeed=maxSpeed, minSpeed=minSpeed, avgSpeed=avgSpeed)

@app.route('/chartSpeed', methods=['GET'])
def chartSpeed():
    db = get_db()
    dropViewSQL = "DROP VIEW IF EXISTS avgByCarType;"
    createViewSQL = """CREATE VIEW avgByCarType AS 
    SELECT AVG(SPEED), Cartype
    FROM TrafficData
    GROUP by Cartype;"""
    sql = "SELECT * FROM avgByCarType"
    cur = db.cursor()
    cur.execute(dropViewSQL)
    cur.execute(createViewSQL)
    cur.execute(sql)
    result = cur.fetchall()
    labels = [row[1] for row in result]
    data = [str(row[0]) for row in result]
    db.commit()
    return render_template('chart.html', labels=labels, values=data)

def getMaxSpeed(db):
    dropViewSQL = "DROP VIEW IF EXISTS maxVelocity;"
    createViewSql = "CREATE VIEW maxVelocity as SELECT MAX(Speed) FROM TrafficData;"
    sql = "SELECT * from maxVelocity;"
    cur = db.cursor()
    cur.execute(dropViewSQL)
    cur.execute(createViewSql)
    cur.execute(sql)
    result = cur.fetchone()
    db.commit()
    return result[0]
def getMinSpeed(db):
    dropViewSQL = "DROP VIEW IF EXISTS minVelocity;"
    createViewSql = "CREATE VIEW minVelocity as SELECT min(Speed) FROM TrafficData;"
    sql = "SELECT * from minVelocity;"
    cur = db.cursor()
    cur.execute(dropViewSQL)
    cur.execute(createViewSql)
    cur.execute(sql)
    result = cur.fetchone()
    db.commit()
    return result[0]
def getAvgSpeed(db):
    dropViewSQL = "DROP VIEW IF EXISTS avgVelocity;"
    createViewSql = "CREATE VIEW avgVelocity as SELECT AVG(Speed) FROM TrafficData;;"
    sql = "SELECT * from avgVelocity;"
    cur = db.cursor()
    cur.execute(dropViewSQL)
    cur.execute(createViewSql)
    cur.execute(sql)
    result = cur.fetchone()
    db.commit()
    return result[0]

if __name__ == '__main__':
    context = ('myCert.crt', 'myKey.key')
    app.run(host='0.0.0.0', port=8080, debug=True,ssl_context = context)