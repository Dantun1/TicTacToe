import sqlite3
from contextlib import contextmanager
from pathlib import Path
from sqlite3 import Error
from typing import ContextManager

DB_PATH = Path(__file__).parent.parent / "data" / "db.sqlite3"


class Database:
    """
    Database wrapper class for facilitating connections.

    Methods:
        connect: Get a connection object to the database
        get_connection: Context manager alternative for getting a connection object (recommended)
    """

    def __init__(self, db_path: Path = DB_PATH) -> None:
        self.db_path = db_path

    def connect(self) -> sqlite3.Connection:
        """
        Request a connection to the database

        Returns:
            sqlite3.Connection: connection to the sqlite3 database
        """
        try:
            return sqlite3.connect(self.db_path)
        except Error as e:
            raise Error(f"Error connecting to database {e}")

    @contextmanager
    def get_connection(self) -> ContextManager[sqlite3.Connection]:
        """
        Get a connection to the database using a context manager

        Yields:
            sqlite3.Connection: connection to the sqlite3 database
        Raises:
            sqlite3.Error: If an error occurs while connecting or using the database.
        """
        try:
            conn = self.connect()
            yield conn
        except Error as e:
            raise Error(f"Error interacting with database {e}")
        finally:
            conn.close()
