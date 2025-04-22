import sqlite3

def create_tables():
    conn = sqlite3.connect(db_filename)
    with open("system_database/db_setup/init_stat_tree.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 setup_database.py [db_filename]")
    else:
        create_tables(sys.argv[1])
