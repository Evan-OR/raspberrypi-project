# Script to be ran on the ol' pie
import time
# from sense_hat import SenseHat
from datetime import datetime
import random

#  [datetime.now().isoformat(), s.get_temperature()]

import socketio


sio = socketio.Client()

sio.connect('http://localhost:5000')

while True:
    temperature_data = {
        "tempData": [345634563456, 28]
    }
    sio.emit('receive_data', temperature_data)
    print("Sent message:", temperature_data)
    time.sleep(1)