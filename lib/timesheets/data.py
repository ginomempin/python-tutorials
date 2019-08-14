
from datetime import datetime
from pathlib import Path

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show
from bokeh.resources import CDN
from pandas_datareader.data import DataReader
from werkzeug import secure_filename
from werkzeug.datastructures import FileStorage


TIMESHEET_DIR = Path(__file__).absolute().parent


def store_timesheet(file: FileStorage):
    timesheet_name = "uploaded" + secure_filename(file.filename)
    timesheet_path = TIMESHEET_DIR.joinpath(timesheet_name)
    file.save(timesheet_path.as_posix())
    return timesheet_path


def fetch_timesheet():
    # TODO: Allow the user to specify which to download.
    #       For now, just get the first uploaded* file.
    timesheet_list = TIMESHEET_DIR.iterdir()
    for t in timesheet_list:
        if t.name.startswith("uploaded"):
            return t.as_posix()

def prepare_timesheet_plot(path: Path):
    # TODO: Replace sample stock market data with the actual
    #       timesheet data, passed as a path to the file.
    df = DataReader(
        name="AAPL",
        data_source="yahoo",
        start=datetime(2019, 3, 1),
        end=datetime(2019, 3, 31 )
    )
    # print(df)
    # print(df.index)

    def inc_or_dec(c_val, o_val):
        if c_val > o_val:
            return "inc"
        elif c_val < o_val:
            return "dec"
        else:
            return "equ"
    df["Status"] = [inc_or_dec(c, o) for c, o in zip(df["Close"], df["Open"])]
    df["Middle"] = (df["Close"] + df["Open"]) / 2
    df["Change"] = abs(df["Close"] - df["Open"])
    # print(df)

    plot = figure(
        plot_width=1000,
        plot_height=300,
        x_axis_type="datetime",
    )
    plot.title.text = "Timesheet Data"
    plot.segment(
        df.index,           # x-coord of starting point
        df["Low"],          # y-coord of starting point
        df.index,           # x-coord of end point
        df["High"],         # y-coord of end point
        line_color="black"
    )
    plot.rect(
        df.index[df["Status"] == "inc"],        # x-center of rect
        df["Middle"][df["Status"] == "inc"],    # y-center of rect
        12 * 60 * 60 * 1000,                    # width, 12h in ms
        df["Change"][df["Status"] == "inc"],    # height,
        fill_color="green",
        line_color="green"
    )
    plot.rect(
        df.index[df["Status"] == "dec"],        # x-center of rect
        df["Middle"][df["Status"] == "dec"],    # y-center of rect
        12 * 60 * 60 * 1000,                    # width, 12h in ms
        df["Change"][df["Status"] == "dec"],    # height,
        fill_color="red",
        line_color="red"
    )
    # output_file("timesheet.html")
    # show(plot)

    plot_js, plot_html = components(plot)
    # print(js)
    # print(html)

    plot_cdn_js = CDN.js_files
    plot_cdn_css = CDN.css_files
    # print(cdn_js)
    # print(cdn_css)

    return plot_html, plot_js, plot_cdn_css, plot_cdn_js
