import sqlite3

# creates a database file, or connects if it already exists
conn = sqlite3.connect('C:\\Users\\Durun\\OneDrive\\Documents\\term 1 freshman\\c++ projects\\PYTHONGOLDER\\practice.db')


# cursor is what you use to send SQL commands
cursor = conn.cursor()

cursor.execute("DELETE FROM players")

# create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        name TEXT,
        nationality TEXT,
        goals INTEGER
    )
''')

conn.commit()
print("database created")

cursor.execute("INSERT INTO players (name, nationality, goals) VALUES ('Messi', 'Argentina', 12)")

# insert multiple rows at once
players = [
    ('Mbappe', 'France', 10),
    ('Ronaldo', 'Portugal', 8),
    ('Vinicius', 'Brazil', 7),
    ('Kane', 'England', 6),
]
cursor.executemany("INSERT INTO players (name, nationality, goals) VALUES (?, ?, ?)", players)

conn.commit()

cursor.execute('SELECT * FROM players')
row = cursor.fetchall()
for row in row:
    print(row)

cursor.execute('SELECT name, goals FROM players')
row = cursor.fetchall()
for row in row:
    print(row)

cursor.execute('SELECT * FROM players WHERE goals > 7')
row = cursor.fetchall()
for row in row:
    print(row)

cursor.execute('SELECT * FROM players LIMIT 3')
row = cursor.fetchall()
for row in row:
    print(row)





conn.close()
print("data inserted")