# Script to be ran on the ol' pie
import time
from sense_hat import SenseHat
from datetime import datetime
import socketio
import argparse
import sqlite3


parser = argparse.ArgumentParser("raspberrypi_websocket_client")
parser.add_argument("-u", help="Url of the sever", required=True, type=str)
args = parser.parse_args()
print(args.u)

connection = sqlite3.connect("test.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    type TEXT,
    data TEXT,
    timestamp TEXT
)
""")


s = SenseHat()

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")


sio.connect(args.u)


while True:
    timestamp = datetime.now().isoformat()
    tempData = s.get_temperature()
    humidData = s.get_humidity()
    gyroData = s.get_gyroscope()

    data = {
        "tempData": [timestamp, tempData],
        "humidData": [timestamp, humidData],
            "gyroData": gyroData
    }

    db_data = [
        ("temperature", str(tempData), timestamp),
        ("humidity", str(humidData), timestamp),
        ("gyroscope", str(gyroData), timestamp)
    ]

    cursor.executemany(
        "INSERT INTO my_table (type, data, timestamp) VALUES (?, ?, ?)",
        db_data
    )
    connection.commit()

    sio.emit('receive_data', data)
    print("Sent message:", data)
    time.sleep(0.05)
