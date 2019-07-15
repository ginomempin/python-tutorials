# TimeTracker

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

1. [Install Python 3, virtualenv, and virtualenvwrapper](https://github.com/ginomempin/how-to#python)
1. Install the project dependencies from [requirements.txt](./requirements.txt):
    ```shell
    $ pip3 install -r requirements.txt

    ```
1. Install [DB Browser for SQLite](https://sqlitebrowser.org/) (for debugging *.db* files)
1. Build the standalone executable:
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
