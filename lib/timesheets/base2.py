"""
This shows how to use Bokeh to display interactive graphs
and other data visualization tools on modern web browsers.

For more examples:
https://bokeh.pydata.org/en/latest/docs/gallery.html
"""

from bokeh.plotting import figure
from bokeh.io import output_file
from bokeh.io import show
import pandas as pd


# ------------------------------------------------------------------------------
# Data
# ------------------------------------------------------------------------------


df1 = pd.read_csv("sample1.csv")
print(df1.axes)
x1 = df1["Year"]
y1 = df1["Engineering"]

df2 = pd.read_excel("sample2.xlsx")
print(df2.axes)
x2 = df2["Temperature"]
y2 = df2["Pressure"]

df3 = pd.read_csv("sample3.csv", parse_dates=["Date"])
print(df3.axes)
x3 = df3["Date"]
y3 = df3["Close"]

x4 = [0, 5, 9]
y4 = [0, 12, 1]


# ------------------------------------------------------------------------------
# Plot Properties
# ------------------------------------------------------------------------------


def create_figure(title: str, xaxis_label: str, yaxis_label: str):
    fig = figure()

    fig.plot_width = 500
    fig.plot_height = 500

    fig.title.text = title
    fig.title.text_color = "blue"

    fig.xaxis.axis_label = xaxis_label
    fig.xaxis.minor_tick_line_color = "red"

    fig.yaxis.axis_label = yaxis_label
    fig.yaxis.minor_tick_line_color = "red"

    return fig


# ------------------------------------------------------------------------------
# Line Graph
# ------------------------------------------------------------------------------


graph = create_figure("Line Graph", "Year", "Engineering")
graph.line(x1, y1)
output_file("sample_line.html")
show(graph)


# ------------------------------------------------------------------------------
# Glyphs
# ------------------------------------------------------------------------------


graph = create_figure("Triangle Glyphs", "Year", "Engineering")
graph.triangle(x1, y1, size=10, angle=45.0)
output_file("sample_triangle.html")
show(graph)

graph = create_figure("Circle Glyphs", "Temperature (°C)", "Pressure (hPa)")
graph.circle(x2, y2, size=1)
output_file("sample_circle.html")
show(graph)


# ------------------------------------------------------------------------------
# Line Graphs + Glyphs
# ------------------------------------------------------------------------------


graph = create_figure("Line + Circle Glyphs", "Year", "Engineering")
graph.line(x1, y1, color="orange")
graph.circle(x1, y1, size=8)
output_file("sample_combined.html")
show(graph)


# ------------------------------------------------------------------------------
# Time Series
# ------------------------------------------------------------------------------


graph = figure(
    plot_width=1000, plot_height=300,
    x_axis_type="datetime")
graph.title.text = "Time Series"
graph.xaxis.axis_label = "Date"
graph.yaxis.axis_label = "Closed At"
graph.line(x3, y3, color="orange")
output_file("sample_series.html")
show(graph)


# ------------------------------------------------------------------------------
# Patches
# ------------------------------------------------------------------------------


graph = create_figure("Patches", "x", "y")
graph.patch(x4, y4, fill_color="orange")
output_file("sample_patches.html")
show(graph)


# ------------------------------------------------------------------------------
# Quads
# ------------------------------------------------------------------------------


graph = create_figure("Quads", "x", "y")
graph.quad(
    top=[2, 3, 4],          # left edge
    bottom=[1.3, 2.2, 3],   # left edge
    left=[1, 2, 3],         # bottom edge
    right=[1.2, 2.5, 3.7],  # bottom edge
    color="green"
)
output_file("sample_quads.html")
show(graph)
