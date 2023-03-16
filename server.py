from flask import Flask, request
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)