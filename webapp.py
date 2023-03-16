from flask import Flask, render_template
import sys
import mysql.connector


app = Flask(__name__)



def get_db():
   db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Hipolito.88",
      database="db_project_CloudComputing"
   )  
   return db

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
    sql = "SELECT * FROM avgByCarTYPE";
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    labels = [row[1] for row in result]
    data = [str(row[0]) for row in result]
    return render_template('chart.html', labels=labels, values=data)

def getMaxSpeed(db):
    sql = "SELECT * from maxVelocity;"
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    return result[0]
def getMinSpeed(db):
    sql = "SELECT * from minVelocity;"
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    return result[0]
def getAvgSpeed(db):
    sql = "SELECT * from avgVelocity;"
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    return result[0]

if __name__ == '__main__':
    context = ('myCert.crt', 'myKey.key')
    app.run(host='0.0.0.0', port=8080, debug=True,ssl_context = context)