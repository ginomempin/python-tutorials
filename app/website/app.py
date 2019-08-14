
from pathlib import Path
import json
import logging
import sys
LIB_DIR = Path("app.py").parent.joinpath("../../lib").resolve()
sys.path.append(LIB_DIR.as_posix())

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

from emailer.client import send_email
from timesheets.data import prepare_timesheet_plot  # pylint: disable=import-error


# ------------------------------------------------------------------------------
# App Instance
# ------------------------------------------------------------------------------


app = Flask(
    __name__,
    static_url_path="/public",
    static_folder="public",
    template_folder="templates"
)


# ------------------------------------------------------------------------------
# App Logger
# ------------------------------------------------------------------------------


logging.getLogger().setLevel(logging.INFO)


# ------------------------------------------------------------------------------
# App Database
# ------------------------------------------------------------------------------
# TODO: Move to a separate file

APPDB_URI = None

try:
    APP_DIR = Path(__file__).resolve().parent
    APPDB_CONFIG_PATH = APP_DIR.joinpath("appdb.json").as_posix()
    with open(APPDB_CONFIG_PATH, "r") as config_file:
        config = json.load(config_file)
        APPDB_URI = "{}://{}{}@{}/{}".format(
            config['type'],
            config['user'],
            ":{}".format(config['pass']) if config['pass'] else "",
            config['host'],
            config['name']
        )
except:  # pylint: disable=bare-except
    logging.fatal("Cannot read DB config from 'appdb.json' file")

logging.info("APPDB_URI = {}".format(APPDB_URI))
app.config['SQLALCHEMY_DATABASE_URI'] = APPDB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
appdb = SQLAlchemy(app)


class Leave(appdb.Model):
    __tablename__ = "leaves"

    id          = appdb.Column(appdb.Integer, primary_key=True)
    email       = appdb.Column(appdb.String(120), unique=True, nullable=False)
    days_req    = appdb.Column(appdb.Integer)

    # SQLAlchemy automatically creates an implicit __init__ method,
    # with the column names as keyword parameters. If there is a need
    # for a custom __init__, make sure to call super() passing in the
    # original keyword arguments.
    # def __init__(**kwargs):
    #     super().__init__(**kwargs)
    #     # custom code

# ------------------------------------------------------------------------------
# App Routes
# ------------------------------------------------------------------------------


@app.route("/")
def root():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/leave_form', methods=['GET', 'POST'])
def leave_form():
    if request.method == 'POST':
        user_email = request.form['user_email']
        num_days = request.form['num_days']
        logging.info("{} {}".format(user_email, num_days))

        user_leaves = Leave.query.filter_by(email=user_email)
        if user_leaves.count() > 0:
            return render_template(
                "leave_rejected.html",
                email=user_email,
                days=user_leaves.first().days_req)
        else:
            leave_req = Leave(
                email=user_email,
                days_req=num_days
            )
            appdb.session.add(leave_req)
            appdb.session.commit()
            send_email(
                user_email,
                "[TimeTracker] Leave Application Received",
                "Request for <b>{}</b> days was received from <b>{}</b>.".format(
                    num_days, user_email)
            )
            return render_template(
                "leave_applied.html",
                email=user_email)
    else:
        return render_template("leave_form.html")


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


# ------------------------------------------------------------------------------
# Entrypoint
# ------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)
