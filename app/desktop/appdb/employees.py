
import sqlite3

from .basedb import DB


class EmployeesDB(DB):
    """SQLite-backed Database"""

    def __init__(self):
        """Create a DB instance"""
        super().__init__("employees.db")
        self._conn = None
        self._cursor = None

    def connect(self):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()

    def create_table(self):
        self._cursor.execute("CREATE TABLE IF NOT EXISTS employees (\
            eid INTEGER PRIMARY KEY, \
            name TEXT, \
            position TEXT \
        )")
        self._conn.commit()

    def fetch_all(self) -> list:
        self._cursor.execute("SELECT * FROM employees")
        return self._cursor.fetchall()

    def fetch(self, name: str) -> list:
        self._cursor.execute("SELECT * FROM employees WHERE name=?", (name,))
        return self._cursor.fetchall()

    def insert_employee(self, name: str, position: str):
        self._cursor.execute("INSERT INTO employees VALUES (NULL,?,?)", (name, position))
        self._conn.commit()

    def delete_employee(self, eid: int):
        self._cursor.execute("DELETE FROM employees WHERE eid=?", (eid,))
        self._conn.commit()

    def update_employee_name(self, eid: int, name: str):
        self._cursor.execute("UPDATE employees SET name=? WHERE eid=?", (name, eid))
        self._conn.commit()

    def update_employee_position(self, eid: int, position: str):
        self._cursor.execute("UPDATE employees SET position=? WHERE eid=?", (position, eid))
        self._conn.commit()

    def disconnect(self):
        self._conn.close()
