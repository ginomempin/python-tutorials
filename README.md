# TimeTracker

A collection of Python apps for the workplace.

This is an application of the lessons from:  
[The Python Mega Course: Build 10 Real World Applications](https://www.udemy.com/the-python-mega-course/learn/v4/overview)

Contents:

1. [Environment](#environment)
1. [Setup](#setup)
1. [Usage](#usage)

---

### Environment

* Mac OS X
* Python 3.6.4
    * virtualenv 15.1.0
    * pip 10.0.1

### Setup

1. Install Python 3
    * On a Unix-based OS, the system's default Python installation will most likely be Python 2.  
      Check this by running `python --version` on a terminal.
      If it returns `2.x`, **DO NOT** remove/overwrite/uninstall it.  
      The system uses Python 2 for its internal scripts and messing with it may break the OS.  
      Python 3 should be setup as a separate installation.
    * Use [Homebrew](https://docs.brew.sh/Homebrew-and-Python) to take care of the Python setup.
    * Verify the Python 3 installation by doing `which python3` and `python3 --version` on a terminal.
1. [Install pip](https://pip.pypa.io/en/stable/installing/)
1. [Install virtualenv](https://virtualenv.pypa.io/en/stable/)
1. [Install virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/#)
1. Create the directory for storing Python virtual environments.
    * Ex. `mkdir -p ~/.virtualenvs`
1. Add the following to your environment's **.bashrc** (or its equivalent):
    ```
    export VIRTUALENVWRAPPER_PYTHON=$(which python3)
    export WORKON_HOME=~/.virtualenvs
    source /Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenvwrapper.sh
    ```
1. Create the virtual environment for this project's development.
    * Ex. `mkvirtualenv tt`
1. Activate the project's virtual environment.
    * Ex. `workon tt`
    * The environment is activated when you see the `(env-name)` at the start of the prompt.
        ```
        (tt) gino:webapp ARi$
        ```
1. From now on, when a project-specific package needs to be installed using **pip**:
    * Make sure to activate (`workon`) the target virtual environment first.  
      This is the main purpose of using **virtualenv**. It should now prevent accidentally  
      doing `pip install <package>` that overwrites a system package (or a dependency used  
      by other projects). This can verified by comparing the `pip list` output between the
      different virtual environments and the native environment.
    * See the complete list of [virtualenvwrapper commands](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html) for more info.
        * Notable commands:
            * `mkvirtualenv`
            * `lsvirtualenv`
            * `allvirtualenv`
            * `lssitepackages`
            * `workon`
            * `deactivate`
1. Install the rest of the packages from **requirements.txt**.
    * Do `pip install -r requirements.txt`

### Usage

* (TODO)
