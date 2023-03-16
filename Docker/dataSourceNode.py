import random
from datetime import datetime
import time
from urllib import request, parse
import json
import os

def function():
    sensorName = os.environ.get("SENSOR_NAME", "sensor1")
    write_period = int(os.environ.get("WRITE_PERIOD", 5)) 
    while(True):
    
        date = datetime.now()
        formatDate = date.strftime("%Y-%m-%d %H:%M:%S")
        cars = ["Truck","Sedan","SUV","Minivan", "Pickup"]
        selectedCar = cars[random.randint(0,4)]
        speed = random.randint(10,150)

        print(f"Car type: {selectedCar}, SPEED: {speed}, Date: {formatDate}")
        
        data = {"sensorName": sensorName,"type":selectedCar, "speed": speed, "date": formatDate}
        data = json.dumps(data).encode('utf-8')

        url = "http://10.132.174.139:8080/store"
        req = request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        resp=request.urlopen(req)
        time.sleep(write_period)

if __name__ == "__main__":
    function()