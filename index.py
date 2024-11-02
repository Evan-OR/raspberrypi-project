from flask import Flask
from plotly.offline import plot
import plotly.graph_objs as go

fig = go.Figure()
scatter = go.Scatter(
    x=[0, 1, 2, 3],
    y=[0, 1, 2, 3],
    mode="lines",
    name="test",
    opacity=0.8,
    marker_color="green",
)
fig.add_trace(scatter)
fig.update_layout(xaxis_title="X Axis Label", yaxis_title="Y Axis Label")
plt_div = plot(fig, output_type="div")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return plt_div
