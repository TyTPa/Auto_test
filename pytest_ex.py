import pytest
from main import init_db, add_user, get_user,count_vowels

@pytest.fixture
def db_conn():
   conn = init_db()
   yield conn
   conn.close()

def test_add_or_get_user(db_conn):
    add_user(db_conn, "Sasha", 30)
    user = get_user(db_conn, "Sasha")
    assert user == (1, "Sasha", 30)

@pytest.mark.parametrize('test_input,expected', [
    ('level', 2),
    ('python', 1),
    ('racecar', 3),
    ('', 0),
    ('Привет', 2),
    ('вцспс', 0),
    ('добрый ДЕНЬ', 3),
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected