
from pathlib import Path


# TODO: Convert DB implementation to PostgreSQL
class DB():
    """
    Base class for all database implementations

    All common operations (ex. add/insert, delete, etc)
    should be defined here as abstract methods, that
    must be implemented by each data-specific DB impl.

    By default, all *.db files are stored in a data
    directory under the same directory where the main
    app was run.
    """
    def __init__(self, db_path, db_name):
        self._db_dir = Path(db_path).absolute().joinpath("data")
        if not self._db_dir.exists():
            Path.mkdir(self._db_dir)
        self._db = self._db_dir.joinpath(db_name)
        print(f"DB path is set to '{self._db.as_posix()}'")
