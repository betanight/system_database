import sqlite3

conn = sqlite3.connect("infinity_game.db")
cursor = conn.cursor()

# REMOVE duplicate characters, keep first occurrence by name
cursor.execute("""
    DELETE FROM characters
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM characters
        GROUP BY name
    )
""")

conn.commit()
conn.close()
