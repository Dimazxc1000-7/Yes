import sqlite3

class Names:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
def ctu(cursor):
    command = '''
    CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY,
      name TEXT,
      surname TEXT,
      gender TEXT);
    '''
    cursor.execute(command)

def add(cursor, name):
    command = '''
        INSERT INTO users (name, surname, gender) VALUES (?, ?, ?);
        '''
    cursor.execute(command, (name.name, name.surname, name.gender))

def pon(cursor):
    command = '''
    SELECT * FROM users
    '''
    result = cursor.execute(command)
    users = result.fetchall()
    print(users[0])
    print(users[1])
    print(users[2])

if __name__ == '__main__':
    with sqlite3.connect('base.bd') as cursor:
       print(cursor)
       ctu(cursor)
       add(cursor, Names(name='Максим', surname = 'Иванов', gender= 'male'))
       add(cursor, Names(name='Дима', surname='Макаров', gender='male'))
       add(cursor, Names(name='Настя', surname='ЯХЗ', gender='female'))
       pon(cursor)

















