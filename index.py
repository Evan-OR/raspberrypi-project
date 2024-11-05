from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, send
from lib.data import get_html_graph
from lib.graph_data import GraphData
from dotenv import load_dotenv
import os

URL = os.getenv("URL")

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

TEMP_DATA = GraphData(100)
GYRO_DATA = {"x": 0, "y": 0, "z": 0}


@socketio.on("receive_data")
def handle_temp_data(data):
    print("Received Data", data)
    TEMP_DATA.add(data["tempData"])

    message = {"tempData": TEMP_DATA.get(), "gyroData": data["gyroData"]}
    socketio.emit("update_data", message)


@app.route("/")
def hello_world():
    return render_template("index.html", URL=URL)
