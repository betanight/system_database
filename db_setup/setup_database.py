import sqlite3

def create_tables():
    conn = sqlite3.connect("infinity_game.db")
    with open("system_database/init_stat_tree.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
