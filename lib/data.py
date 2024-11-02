from datetime import datetime, timedelta
import random
import plotly.graph_objs as go
from plotly.offline import plot


def make_fake_data(amount_of_data_points):
    current_time = datetime.now()
    time_data = []
    temp_data = []

    for i in range(amount_of_data_points):
        time_data.append(current_time - timedelta(minutes=amount_of_data_points - i))
        temp_data.append(random.randint(18, 22))

    return (time_data, temp_data)


def get_html_graph(x, y):
    fig = go.Figure()
    scatter = go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name="test",
        opacity=0.8,
        marker_color="green",
    )
    fig.add_trace(scatter)
    fig.update_layout(
        title="Raspberry Pi Temperature Data",
        xaxis_title="Time",
        yaxis_title="Temp",
        template="plotly_dark",
    )
    html_graph = plot(fig, output_type="div")
    return html_graph
