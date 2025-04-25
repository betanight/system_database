const sqlite3 = require("sqlite3").verbose();

function allocateInitialSkillPoints(dbFile, skillChoices) {
  const db = new sqlite3.Database(dbFile);

  const primaryStats = {
    Strength: "strength_skills",
    Dexterity: "dexterity_skills",
    Constitution: "constitution_skills",
    Intelligence: "intelligence_skills",
    Wisdom: "wisdom_skills",
    Charisma: "charisma_skills"
  };

  const secondaryStats = {
    Instinct: "instinct_skills",
    Presence: "presence_skills",
    Spirit: "spirit_skills",
    Willpower: "willpower_skills"
  };

  db.serialize(() => {
    const allStats = { ...primaryStats, ...secondaryStats };

    for (const stat in allStats) {
      const skillTable = allStats[stat];
      const selectedSkill = skillChoices[stat];

      if (!selectedSkill) {
        console.warn(`No skill selected for ${stat}. Skipping.`);
        continue;
      }

      const query = `
        UPDATE ${skillTable}
        SET effective_value = effective_value + 1
        WHERE name = ?
      `;

      db.run(query, [selectedSkill], function (err) {
        if (err) {
          console.error(`Error updating ${selectedSkill} in ${skillTable}:`, err.message);
        } else if (this.changes === 0) {
          console.warn(`Skill '${selectedSkill}' not found in ${skillTable}.`);
        } else {
          console.log(`Allocated 1 point to '${selectedSkill}' in ${stat}.`);
        }
      });
    }
  });

  db.close();
}

module.exports = { allocateInitialSkillPoints };
