from flask import Flask, render_template
from flask_socketio import SocketIO
from lib.graph_data import GraphData
from datetime import datetime, timedelta
import os

URL = os.getenv("URL")

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

TEMP_DATA = GraphData()
HUMIDITY_DATA = GraphData()


@socketio.on("receive_data")
def handle_temp_data(data):
    print("Received Data", data)

    timestamp, _ = data["tempData"]
    last_data_point = TEMP_DATA.get_last()

    if not last_data_point or abs(
        datetime.fromisoformat(timestamp) - datetime.fromisoformat(last_data_point[0])
    ) >= timedelta(seconds=1):
        TEMP_DATA.add(data["tempData"])
        HUMIDITY_DATA.add(data["humidData"])

    message = {
        "tempData": TEMP_DATA.get_formatted_data(),
        "humidData": HUMIDITY_DATA.get_formatted_data(),
        "gyroData": data["gyroData"],
    }
    socketio.emit("update_data", message)


@app.route("/")
def hello_world():
    return render_template("index.html", URL=URL)
