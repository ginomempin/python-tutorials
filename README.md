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
* Homebrew 2.1.1
* Python 3.7.3, pip 19.1, virtualenv 16.5.0
* [requirements.txt](./requirements.txt)

## Setup

1. Install Python 3
    * On a Unix-based OS, the system's default Python installation might be Python 2. Check this by running `python --version` on a terminal. If this is so, install Python 3 but **DO NOT REMOVE/OVERWRITE/UNINSTALL** the old Python 2. The system uses Python 2 for its internal scripts and removing it may break the OS installation.
    * Use [Homebrew](https://docs.brew.sh/Homebrew-and-Python)
    * Verify the Python 3 installation by running `which python3` and `python3 --version` on a terminal.
1. Install [pip](https://pip.pypa.io/en/stable/installing/)
1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/)
    * Do `pip install virtualenv`
    * The purpose of using a **virtualenv** is to:
        * Allow different Python projects to have different packages
        * Prevent from accidentally overwriting a system package
1. Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/#)
    * Do `pip install virtualenvwrapper`
    * Notable [virtualenvwrapper commands](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html):
        * `mkvirtualenv`
        * `lsvirtualenv`
        * `lssitepackages`
        * `workon`
        * `deactivate`
1. Create the directory for storing Python virtual environments
    ```bash
    $ mkdir -p ~/.virtualenvs

    ```
1. Add the following to your environment's **.bash_profile** (or its equivalent):
    ```bash
    export VIRTUALENVWRAPPER_PYTHON=$(which python3)
    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

    ```
1. Create the virtual environment for this project.
    ```bash
    $ mkvirtualenv timetracker

    ```
1. Activate the project's virtual environment.
    ```bash
    $ workon timetracker

    ```
1. Install the rest of the packages from [requirements.txt](./requirements.txt):
    ```bash
    $ pip3 install -r requirements.txt

    ```

## Usage

### blocker

1. Open [blocker.py](./productivity/blocker/blocker.py)
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
