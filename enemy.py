import random

# Enemy Class    
class Enemy():
    def __init__(self, name, strength, defense, health, exp):
        self.health = health
        self.name = name
        self.strength = strength
        self.defense = defense
        self.exp = exp
    def attack(self, other):
        # Roll For Enemy Attack
        iRand = int(random.randint(1, 100))
        # Hit If Below: 100 - player.defense
        if iRand <= (100 - other.defense):
            iDmg = int(random.randint(1, self.strength))
            print("The {0.name} hits for {1} damage.".format(self, iDmg))
            other.health -= iDmg
        else:
            print("The {0.name} misses...".format(self))
