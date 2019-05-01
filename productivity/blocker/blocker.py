#!/usr/local/bin/python3

###############################################################
#                        IMPORTS                              #
###############################################################


import time
from datetime import datetime as dt


###############################################################
#                        DEFINES                              #
###############################################################

DEBUG = False

# Set the path to the network hosts file.
if DEBUG:
    HOSTS_FILE = "hosts"
else:
    HOSTS_FILE = "/etc/hosts"

# Set which websites to block and which error
# page to redirect them to.
ERROR_PAGE = "127.0.0.1"
BLOCK_LIST = [
    # FACEBOOK
    "www.facebook.com",
    "facebook.com",
    # YOUTUBE
    "www.youtube.com",
    "youtube.com"
]

# Set the working hours during which the URLs
# from the BLOCK_LIST should be blocked. All
# values should be in 24H format.
HOUR_S = 8
HOUR_E = 17

# Set the interval (in seconds) when the script
# should check the current time and update its
# behavior (if necessary)
INTERVAL_SEC = 5


###############################################################
#                         FUNCTIONS                           #
###############################################################


def is_working_hours():
    return HOUR_S < dt.now().hour < HOUR_E


def block_websites():
    with open(HOSTS_FILE, "r+") as hosts:
        content = hosts.readlines()
        for website in BLOCK_LIST:
            if not any(website in line for line in content):
                hosts.write("{}\t{}\n".format(ERROR_PAGE, website))


def allow_websites():
    with open(HOSTS_FILE, "r+") as hosts:
        content = hosts.readlines()
        hosts.seek(0)
        hosts.truncate()
        for line in content:
            if not any(website in line for website in BLOCK_LIST):
                hosts.write(line)


###############################################################
#                           MAIN                              #
###############################################################


while True:
    if is_working_hours():
        block_websites()
    else:
        allow_websites()

    time.sleep(INTERVAL_SEC)
