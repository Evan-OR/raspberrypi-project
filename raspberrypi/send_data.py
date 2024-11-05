# Script to be ran on the ol' pie
import time
from sense_hat import SenseHat
from datetime import datetime
import socketio

s = SenseHat()

sio = socketio.Client()

sio.connect('http://192.168.51.127:5000')

while True:
    temperature_data = {
        "tempData": [datetime.now().isoformat(), s.get_temperature()]
    }
    sio.emit('receive_data', temperature_data)
    print("Sent message:", temperature_data)
    time.sleep(1)