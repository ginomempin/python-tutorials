
from pathlib import Path
import sys
LIB_DIR = Path("app.py").parent.joinpath("../../lib").resolve()
sys.path.append(LIB_DIR.as_posix())

from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for

from timesheets.data import prepare_timesheet_plot  # pylint: disable=import-error


app = Flask(
    __name__,
    static_url_path="/public",
    static_folder="public",
    template_folder="templates"
)


@app.route("/")
def root():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/timesheet')
def timesheet():
    plot = prepare_timesheet_plot()
    html, js, cdn_css, cdn_js = plot
    return render_template(
        "timesheet.html",
        html=html,
        js=js,
        cdn_css=cdn_css,
        cdn_js=cdn_js
    )


if __name__ == "__main__":
    app.run(debug=True)
