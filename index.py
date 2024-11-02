from flask import Flask, request, jsonify, render_template
from plotly.offline import plot
import plotly.graph_objs as go
from lib.data import get_html_graph, make_fake_data
from lib.graph_data import GraphData


app = Flask(__name__)

real_temp_data = GraphData(100)


@app.route("/")
def hello_world():
    time_data, temp_data = make_fake_data(20)

    html_graph = get_html_graph(time_data, temp_data)

    return render_template("index.html", graph=html_graph)


@app.route("/api/data", methods=["POST", "GET"])
def test():
    if request.method == "GET":
        return jsonify({"data": real_temp_data})
    elif request.method == "POST":
        data = request.json

        real_temp_data.add(data["tempData"])
        print(real_temp_data.get())  # remove this, just fir debugg
        return "added data bruv, thumbs up emoji"
