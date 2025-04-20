class Character:
    def __init__(self, name):
        self.name = name

        self.strength = 1
        self.dexterity = 1
        self.constitution = 1
        self.intelligence = 1
        self.wisdom = 1
        self.charisma = 1

        self.willpower = 0
        self.spirit = 0
        self.instinct = 0
        self.presence = 0

    def increase_stat(self, stat_name, amount):
        if hasattr(self, stat_name):
            setattr(self, stat_name, getattr(self, stat_name) + amount)

    def decrease_stat(self, stat_name, amount):
        if hasattr(self, stat_name):
            setattr(self, stat_name, getattr(self, stat_name) - amount)

    def set_stat(self, stat_name, new_value):
        if hasattr(self, stat_name):
            setattr(self, stat_name, new_value)

    def get_stat(self, stat_name):
        if hasattr(self, stat_name):
            return getattr(self, stat_name)
        return None
