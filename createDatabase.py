import mysql.connector


def create_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP database IF EXISTS db_project_CloudComputing")
    mycursor.execute("CREATE DATABASE db_project_CloudComputing")
    mydb.close()


def createTable():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db_project_CloudComputing"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS TrafficData")
    mycursor.execute("""CREATE TABLE TrafficData (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        CarType VARCHAR(10) NOT NULL,
        Speed INT NOT NULL,
        Date_Time DATETIME NOT NULL, 
        SensorName VARCHAR(10) NOT NULL DEFAULT "sensor1")""")
    mydb.close()

if __name__ == '__main__':
    create_db()
    createTable()
