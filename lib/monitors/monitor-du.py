#!/usr/bin/python3

from datetime import datetime
from email.mime.text import MIMEText
import json
import logging
from pathlib import Path
import re
import smtplib
import subprocess


DIVIDER = "-" * 10

SERVER_DETAILS = {
    "name" : "",
    "port" : 0
}
CLIENT_DETAILS = {
    "user" : "",
    "pass" : ""
}
SUBSCRIBER = "someone@somewhere.com"
DIRECTORIES = []

WARN_SIZE_GB = "100G"
WARN_SIZE_GB_VAL = 10

MAX_NUM_USAGES = 30

try:
    this_dir = Path(__file__).resolve().parent
    config_path = this_dir.joinpath("monitor-du-config.json").as_posix()
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
        server_config = config["server"]
        for key in SERVER_DETAILS:
            SERVER_DETAILS[key] = server_config[key]
        client_config = config["client"]
        for key in CLIENT_DETAILS:
            CLIENT_DETAILS[key] = client_config[key]
        SUBSCRIBER = config["subscriber"]
        DIRECTORIES = config["directories"]
        WARN_SIZE_GB = config["limits"]["warn_size_gb"]
        WARN_SIZE_GB_VAL = int(re.sub("[^0-9]", "", WARN_SIZE_GB))
except:  # pylint: disable=bare-except
    logging.fatal("Cannot setup email credentials.")
    logging.fatal("Make sure a 'monitor-du-config.json' file exists.")
    exit(1)


def get_disk_usage():
    summary = []
    max_usage = 0

    for dir_ in DIRECTORIES:
        du_cmd = "/usr/bin/du {} -h".format(dir_)
        du_proc = subprocess.Popen(
            du_cmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        sort_cmd = "sort -h"
        sort_proc = subprocess.Popen(
            sort_cmd.split(),
            stdin=du_proc.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        stdout, _ = sort_proc.communicate()
        summary.append(dir_)
        summary.append(DIVIDER)
        top_usages = []
        all_usages = stdout.split(b"\n")
        num_usages = len(all_usages)
        count = MAX_NUM_USAGES if num_usages >= 20 else MAX_NUM_USAGES
        for s in all_usages[-count:]:
            if len(s.strip()) > 0:
                top_usages.append(s.decode("utf-8"))
        top_usages.reverse()
        summary.extend(top_usages)

        top_usage_str = top_usages[0]
        top_usage_val = int(re.sub("[^0-9]", "", top_usage_str))
        if top_usage_val > max_usage:
            max_usage = top_usage_val

    return summary, max_usage


def send_email(body):
    body_fmt = "This is an auto-generated message.<br>"
    body_fmt += "See &lt;BuildPC&gt;:/home/common/monitor-du.py<br>"
    body_fmt += "<br>"

    dt_fmt = "%Y/%m/%d %I:%M:%S%p"
    body_fmt += "As of <b>{}</b><br>".format(datetime.now().strftime(dt_fmt))
    body_fmt += "The disk usage has exceeded the warning limit of <b>{}</b>.<br>".format(WARN_SIZE_GB)
    body_fmt += "<br>"
    for line in body:
        if line == DIVIDER:
            body_fmt += "<hr>"
        else:
            body_fmt += line
            body_fmt += "<br>"

    msg = MIMEText(body_fmt, "html")
    msg["Subject"] = "[CommonPF] Build PC Disk Usage"
    msg["From"] = CLIENT_DETAILS["user"]
    msg["To"] = SUBSCRIBER

    client = smtplib.SMTP(
        SERVER_DETAILS["name"],
        SERVER_DETAILS["port"]
    )
    client.ehlo()
    client.starttls()
    client.ehlo()
    client.login(
        CLIENT_DETAILS["user"],
        CLIENT_DETAILS["pass"]
    )
    client.send_message(msg)

if __name__ == "__main__":
    du_all, du_max = get_disk_usage()
    if du_max > WARN_SIZE_GB_VAL:
        send_email(du_all)
