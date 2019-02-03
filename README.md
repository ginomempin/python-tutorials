# TimeTracker

A collection of Python apps for the workplace.

This is an application of the lessons from:
[The Python Mega Course: Build 10 Real World Applications](https://www.udemy.com/the-python-mega-course/learn/v4/overview)

## Environment

* macOS 10.13.6
* Python 3.7.2
    * virtualenv 16.0.0
    * pip 18.1

## Setup

1. Install Python 3
    * On a Unix-based OS, the system's default Python installation might be Python 2.
      Check this by running `python --version` on a terminal.
      If this is so, install Python 3 but **DO NOT REMOVE/OVERWRITE/UNINSTALL** the old Python 2.
      The system uses Python 2 for its internal scripts and removing it may break the OS installation.
    * Verify the Python 3 installation by running `which python3` and `python3 --version` on a terminal.
1. Install [pip](https://pip.pypa.io/en/stable/installing/)
1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/)
    * Do `pip install virtualenv`.
1. Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/#)
    * Do `pip install virtualenvwrapper`.
1. Create the directory for storing Python virtual environments.
    * Ex. `mkdir -p ~/.virtualenvs`
1. Add the following to your environment's **.bashrc** (or its equivalent):
    ```bash
    export VIRTUALENVWRAPPER_PYTHON=$(which python3)
    export WORKON_HOME=~/.virtualenvs
    source /Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenvwrapper.sh
    ```
1. Create the virtual environment for this project's development.
    * Ex. `mkvirtualenv tt`
1. Activate the project's virtual environment.
    * Ex. `workon tt`
    * The environment is activated when you see the `(env-name)` at the start of the prompt.
        ```bash
        (tt) gino@Work$
        ```
1. From now on, when a project-specific package needs to be installed using **pip**:
    * The purpose of using a **virtualenv** is to:
        * Allow different Python projects to have different packages
        * Prevent from accidentally doing `pip install <package>` that overwrites a system package
    * Notable [virtualenvwrapper commands](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html).
        * `mkvirtualenv`
        * `lsvirtualenv`
        * `allvirtualenv`
        * `lssitepackages`
        * `workon`
        * `deactivate`
1. Install the rest of the packages from **requirements.txt**.
    * Do `pip install -r requirements.txt`

## Usage

* (TODO)
