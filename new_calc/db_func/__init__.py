import os
import sqlite3

DB_FILE_PATH = os.path.join(os.getcwd(), 'database', 'mydb.db')
print(DB_FILE_PATH)


def check_login(login):
    connection = sqlite3.connect(DB_FILE_PATH)
    cursor = connection.cursor()
    query = f'SELECT login FROM users WHERE login == "{login}"'
    cursor.execute(query)
    cursor_result = cursor.fetchone()
    if cursor_result:
        result = True
    else:
        result = False
    return result

    '''function to check the login in the database'''


def check_password(password):
    '''function to check the password in the database'''
    pass


if __name__ == "__main__":
    check_login('admin')
