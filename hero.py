class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defence = 1
        self.crit_chance = 0.25 # Chance in Percentage (0.25 = 25% chance of crit)
        self.crit_damage = 1.5 # Multipler rate (etc 1.5x more damage)
        # defence = 1
        # crit_chance = 0.25 # Chance in Percentage (0.25 = 25% chance of crit)
        # crit_damage = 1.5 # Multipler rate (etc 1.5x more damage)


