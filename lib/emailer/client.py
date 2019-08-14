
from email.mime.text import MIMEText
import json
import logging
from pathlib import Path
import smtplib

CLIENT_ADDR = None
CLIENT_PASS = None

try:
    this_dir = Path(__file__).resolve().parent
    config_path = this_dir.joinpath("client.json").as_posix()
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
        CLIENT_ADDR = config["addr"]
        CLIENT_PASS = config["pass"]
except:  # pylint: disable=bare-except
    logging.fatal("Cannot read email credentials from 'client.json' file")


def send_email(addr, subj, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subj
    msg['To'] = addr
    msg['From'] = CLIENT_ADDR

    client = smtplib.SMTP('smtp.gmail.com', 587)
    client.ehlo()
    client.starttls()
    client.login(CLIENT_ADDR, CLIENT_PASS)

    client.send_message(msg)
