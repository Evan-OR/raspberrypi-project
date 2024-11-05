# Script to be ran on the ol' pie
import time
from sense_hat import SenseHat
from datetime import datetime
import socketio
import argparse

parser = argparse.ArgumentParser("raspberrypi_websocket_client")
parser.add_argument("-u", help="Url of the sever", required=True, type=str)
args = parser.parse_args()
print(args.u)

s = SenseHat()

sio = socketio.Client()

sio.connect(args.u)

while True:
    temperature_data = {
        "tempData": [datetime.now().isoformat(), s.get_temperature()],
        "gyroData": {'x': 0.06546039879322052, 'y': 0.21827052533626556, 'z': -1.0255765914916992}
    }
    sio.emit('receive_data', temperature_data)
    print("Sent message:", temperature_data)
    time.sleep(1)