
from pathlib import Path


class DB():
    """
    Base class for all database implementations

    All common operations (ex. add/insert, delete, etc)
    should be defined here as abstract methods, that
    must be implemented by each data-specific DB impl.

    By default, all *.db files are stored in the same
    directory as this file.
    """

    def __init__(self, db_name):
        self._db_dir = Path(__file__).absolute().parent
        self._db = self._db_dir.joinpath(db_name)
