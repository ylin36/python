# context manager without contextlib

import sqlite3


class DataConn:
    """"""

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """
        Open the database connection
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        self.conn.close()
        if exc_val:
            raise

# context manager with contextlib
from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("Error")
    finally:
        print('Closing...')
        f_obj.close()

if __name__ == '__main__':

    db = "test.db"
    with DataConn(db) as conn:
        cursor = conn.cursor()

    with file_open('test.txt') as fobj:
        fobj.write('Testing context managers')