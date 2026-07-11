import pandas as pd
import sqlite3

df = pd.read_csv(r'C:\Users\Durun\OneDrive\Documents\term 1 freshman\c++ projects\PYTHONGOLDER\summerpractice\fifa_world_cup_2026_player_performance.csv')

conn = sqlite3.connect(r'C:\Users\Durun\OneDrive\Documents\term 1 freshman\c++ projects\PYTHONGOLDER\worldcup.db')

df.to_sql('players', conn, if_exists= 'replace', index= False)

conn.commit()
cursor = conn.cursor()

cursor.execute('SELECT player_name,total_goals_tournament FROM players ORDER BY total_goals_tournament DESC LIMIT 10')
rows = cursor.fetchall()
for row in rows:
    print(row)
print()
cursor.execute('SELECT SUM(total_goals_tournament) as total_goals, nationality FROM players GROUP BY nationality ORDER BY total_goals DESC')
rows = cursor.fetchall()
for row in rows:
    print(f'{row[1]} : {row[0]}')

conn.close()