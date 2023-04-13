import random
from datetime import datetime
import time
import requests
import json
import os
import ssl

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

        url = "https://10.132.174.72:8080/store"

        
        cert_path = "./myCert.crt"
        key_path = "./myKey.key"
        ssl_context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_cert_chain(certfile=cert_path, keyfile=key_path)
        response = requests.post(url, data=data, headers={'Content-Type': 'application/json'},cert=(cert_path, key_path), verify=cert_path)
        time.sleep(write_period)

if __name__ == "__main__":
    function()