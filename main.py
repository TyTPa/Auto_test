import sqlite3

def init_db():
   conn = sqlite3.connect(':memory:')
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER)
   ''')
   return conn
def add_user(conn, name, age):
   cursor = conn.cursor()
   cursor.execute('''
   INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
   conn.commit()

def get_user(conn, name):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users WHERE name=?''', (name,))
    return cursor.fetchone()

def modulo(a, b):
    """
    Вычисляет остаток от деления a на b.

    Args:
        a (int): Делимое
        b (int): Делитель

    Returns:
        int: Остаток от деления a на b

    Raises:
        ZeroDivisionError: Если b равно 0
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a % b

def count_vowels(text):
    """
    Считает количество гласных букв в строке.

    Args:
        text (str): Строка для анализа

    Returns:
        int: Количество гласных букв в строке
    """
    vowels = "aeiouаеёиоуыэюя"  # Гласные буквы английского и русского алфавитов
    count = 0

    for char in text.lower():  # Приводим к нижнему регистру для унификации
        if char in vowels:
            count += 1

    return count

def isPalindrome(s): # переворачивает слово
    return s == s[::-1]