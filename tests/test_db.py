import db
import pytest


@pytest.fixture
def db_conn():
    """
    Instantiate a database wrapper object
    """
    return db.Database(":memory:")


def test_connect_with_context_manager(db_conn):
    with db_conn.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        assert cursor.fetchone()[0] == 1

def test_connect_as_connection_object(db_conn):
    conn = db_conn.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT 1;")
    assert cursor.fetchone()[0] == 1
    conn.close()



