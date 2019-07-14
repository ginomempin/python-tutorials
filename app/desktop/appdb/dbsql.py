
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
        self._cursor.execute("CREATE TABLE IF NOT EXISTS employees (name TEXT, employee_id TEXT, position TEXT)")
        self._conn.commit()

    def fetch_all(self) -> list:
        self._cursor.execute("SELECT * FROM employees")
        return self._cursor.fetchall()

    def insert_employee(self, name: str, employee_id: str, position: str):
        self._cursor.execute("INSERT INTO employees VALUES (?,?,?)", (name, employee_id, position))
        self._conn.commit()

    def delete_employee(self, employee_id: str):
        self._cursor.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))
        self._conn.commit()

    def update_employee_name(self, employee_id: str, name: str):
        self._cursor.execute("UPDATE employees SET name=? WHERE employee_id=?", (name, employee_id))
        self._conn.commit()

    def update_employee_position(self, employee_id: str, position: str):
        self._cursor.execute("UPDATE employees SET position=? WHERE employee_id=?", (position, employee_id))
        self._conn.commit()

    def disconnect(self):
        self._conn.close()
