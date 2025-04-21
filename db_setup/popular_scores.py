import sqlite3

conn = sqlite3.connect("infinity_game.db")
cursor = conn.cursor()

primary_stats = [
    'Strength',
    'Dexterity',
    'Constitution',
    'Intelligence',
    'Wisdom',
    'Charisma'
]

secondary_stats = [
    'Willpower',
    'Spirit',
    'Instinct',
    'Presence'
]

cursor.executemany("INSERT OR IGNORE INTO primary_scores (name) VALUES (?)", [(stat,) for stat in primary_stats])
cursor.executemany("INSERT OR IGNORE INTO secondary_scores (name) VALUES (?)", [(stat,) for stat in secondary_stats])

conn.commit()
conn.close()
