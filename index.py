from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, send
from lib.data import get_html_graph
from lib.graph_data import GraphData
from dotenv import load_dotenv
import os

URL = os.getenv("URL")

app = Flask(__name__)
socketio = SocketIO(app)

real_temp_data = GraphData(100)


@socketio.on("receive_data")
def handle_temp_data(data):
    data = data["tempData"]
    real_temp_data.add(data)

    print(f"Received temperature data - Timestamp: {data[0]}, Temperature: {data[1]}")

    message = {"tempData": real_temp_data.get()}
    socketio.emit("update_data", message)


@app.route("/")
def hello_world():
    return render_template("index.html", URL=URL)
