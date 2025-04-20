import sqlite3

conn = sqlite3.connect("infinity_game.db")

with open("init_stat_tree.sql", "r") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()