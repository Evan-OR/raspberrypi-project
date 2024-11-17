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

@sio.event
def connect():
    print("Connected to server")


sio.connect(args.u)

while True:
    timestamp = datetime.now().isoformat()
    data = {
        "tempData": [timestamp, s.get_temperature()],
        "humidData": [timestamp, s.get_humidity()],
        "gyroData": s.get_gyroscope()
    }
    sio.emit('receive_data', data)
    print("Sent message:", data)
    time.sleep(0.05)
    