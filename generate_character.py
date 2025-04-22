import sqlite3
import sys
import os

# Ensure skill modules are recognized as a package
skills_init_path = os.path.join(os.path.dirname(__file__), "skills", "__init__.py")
if not os.path.exists(skills_init_path):
    open(skills_init_path, 'a').close()

# Import character and score setup functions
from system_database.db_setup.setup_database import create_tables
from system_database.db_setup.popular_scores import insert_primary_scores, insert_secondary_scores
from system_database.db_setup.create_skill_tables import create_skill_tables
from system_database.db_setup.character_functions import create_character

# Import all skill inserts
from system_database.skills.charisma import insert_charisma_skills
from system_database.skills.constitution import insert_constitution_skills
from system_database.skills.dexterity import insert_dexterity_skills
from system_database.skills.intelligence import insert_intelligence_skills
from system_database.skills.instinct import insert_instinct_skills
from system_database.skills.presence import insert_presence_skills
from system_database.skills.spirit import insert_spirit_skills
from system_database.skills.strength import insert_strength_skills
from system_database.skills.willpower import insert_willpower_skills
from system_database.skills.wisdom import insert_wisdom_skills

def generate_character_db(character_name):
    create_tables()
    insert_primary_scores()
    insert_secondary_scores()
    create_skill_tables()

    insert_charisma_skills()
    insert_constitution_skills()
    insert_dexterity_skills()
    insert_intelligence_skills()
    insert_instinct_skills()
    insert_presence_skills()
    insert_spirit_skills()
    insert_strength_skills()
    insert_willpower_skills()
    insert_wisdom_skills()

    # Avoid duplicates
    conn = sqlite3.connect("infinity_game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM characters WHERE name = ?", (character_name,))
    if cursor.fetchone():
        print(f"Character '{character_name}' already exists. Skipping creation.")
    else:
        create_character(character_name)
        print(f"You have created a new character at level 0! Welcome, {character_name}.")
    conn.close()

if __name__ == "__main__":
    character_name = input("You have created a new character at level 0! What is this adventurer's name?: ")
    generate_character_db(character_name)
