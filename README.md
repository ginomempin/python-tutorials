# Python Tutorials

A collection of Python apps for the workplace.

Contents

* [Environment](#environment)
* [Setup](#setup)
* [Usage](#usage)
    * [blocker](#blocker)
* [References](#references)

## Environment

* macOS 10.13.6
* Homebrew 2.1.7
* Python 3.7.3, pip 19.1, virtualenv 16.5.0
* OpenCV 4.1.0
* [requirements.txt](./requirements.txt)

## Setup

1. [Setup Python 3 and a virtual environment](https://github.com/ginomempin/how-to#python)
1. Setup the project dependencies from [requirements.txt](./requirements.txt):
    ```shell
    $ pip3 install -r requirements.txt

    ```
1. Setup the DB backend:
    * postgresql
        1. Install with HomeBrew:
            ```shell
            $ brew install postgresql
            $ pg_ctl -D /usr/local/var/postgres/ start && brew services start postgresql

            ```
        1. Create the user specific for this project's database
            ```shell
            $ createuser <user_name> --login --createdb

            ```
        1. Install [pgAdmin](https://www.pgadmin.org/download/pgadmin-4-macos/)
        1. Create the database (make sure to link the just-created user)
        1. Run the [setup script](./app/website/setup_db.py) to create the tables
    * sqlite3
        1. Install with HomeBrew:
            ```shell
            $ brew install sqlite

            ```
        1. Install [DB Browser for SQLite](https://sqlitebrowser.org/) (for debugging *.db* files)
1. Setup the email client
    * Go to *lib/emailer*
    * Create a *client.json* file with the following contents:
        ```json
        {
            "addr": "your@email.address",
            "pass": "password"
        }

        ```
    * Make sure to **NEVER** commit this file to the repository.
    * If using GMail, make sure to enable [Less secure app access](https://support.google.com/accounts/answer/6010255?hl=en&authuser=1)
1. Build the standalone executable
    ```shell
    $ cd TimeTracker
    $ pyinstaller --clean \
                  --onefile \
                  --noconfirm \
                  --distpath=app/desktop/dist \
                  --workpath=app/desktop/dist/build \
                  --specpath=app/desktop \
                  --name=app \
                  app/desktop/app.py

    ```

## Usage

### website

TODO

### blocker

1. Open [blocker.py](./lib/productivity/blocker/blocker.py)
1. Set the script parameters:
    * Set `DEBUG` to `False` to use the actual *hosts* file
    * Set which websites to block in `BLOCK_LIST`
    * Set the blocking period in `HOUR_S` and `HOUR_E`
1. Run
    * Manually
        ```
        $ sudo python3 blocker.py

        ```
    * As a daemon or a background process
        * [Running Python in background on OS X](https://stackoverflow.com/q/9522324/2745495)
        * [How to run a Python script in the background even after I logout SSH?](https://stackoverflow.com/q/2975624/2745495)

## References

* [The Python Mega Course: Build 10 Real World Applications](https://www.udemy.com/the-python-mega-course/learn/v4/overview).
