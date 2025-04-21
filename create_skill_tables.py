import sqlite3

conn = sqlite3.connect("infinity_game.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS skill_dependencies (
    skill_id INTEGER NOT NULL,
    depends_on_id INTEGER NOT NULL,
    FOREIGN KEY (skill_id) REFERENCES skills(id),
    FOREIGN KEY (depends_on_id) REFERENCES skills(id),
    PRIMARY KEY (skill_id, depends_on_id)
);

CREATE TABLE IF NOT EXISTS strength_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS dexterity_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS constitution_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS intelligence_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS wisdom_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS charisma_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS willpower_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS spirit_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS instinct_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS presence_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS character_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_table TEXT UNIQUE NOT NULL
);

INSERT OR IGNORE INTO character_skills (skill_table) VALUES
('strength Skills'),
('dexterity Skills'),
('constitution Skills'),
('intelligence Skills'),
('wisdom Skills'),
('charisma Skills'),
('willpower Skills'),
('spirit Skills'),
('instinct Skills'),
('presence Skills');
""")

conn.commit()
conn.close()