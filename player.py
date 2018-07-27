import random

# Player Class    
class Player():
    
    def __init__(self, block, health, maxhealth, defense, kills, biocort, cash, exp, seu, seutotal, weapon, weapondmg, weapontype, clips, healtimes, level, nextlevel):
        self.health = health
        self.block = block
        self.maxhealth = maxhealth
        self.defense = defense
        self.kills = kills
        self.biocort = biocort
        self.cash = cash
        self.exp = exp
        self.seu = seu
        self.seutotal = seutotal
        self.weapon = weapon
        self.weapondmg = weapondmg
        self.weapontype = weapontype
        self.clips = clips
        self.healtimes = healtimes
        self.level = level
        self.nextlevel = nextlevel
        
    # Player Attack Routine
    def attack(self, other):
        # Input - Attack / Block / Heal
        answer = input("What do you want to do (attack, block or heal)? ")
        # Player Attack
        if answer.lower() in ('attack', 'a'):
            # Check SEUs. If below need amount needed for a shot, reload. 
            if self.seutotal < self.seu:
                if self.clips == 0:
                    print("You don't have any ammo...")
                else:
                    self.seutotal = 10
                    self.clips -= 1
                    print("Reloading...")
            else:
                # Use SEUs for Weapon
                self.seutotal -= self.seu
                # Roll For Hit
                iRand = int(random.randint(1, 100))
                if iRand <= ((95 + (self.level * 5)) - other.defense):
                    # Calculate Damage
                    iDmg = int(random.randint(1, self.weapondmg))
                    print("Firing your {0.weapon} you hit for {1} damage.".format(self, iDmg))
                    other.health -= iDmg
                else:
                    print("You miss...")
        # Player Block
        elif answer.lower() in ('block','b'):
            # Roll For Block
            iTest = int(random.randint(1, 100))
            # Low Roll Favors Player
            if iTest <= 10:
                print("You put up your force shiled, smashing the {0.name} in the face.".format(other))
                other.health -= int(random.randint(1, 10))
                self.block = 1
            # High Roll Favors Enemy
            elif iTest >= 90:
                print("You put up your force shiled, but the {0.name} cuts your side.".format(other))
                self.health -= int(random.randint(1, 10))
                self.block = 2
            else:
                print("You put up your force shiled, taking no damage.")
                self.block = 1
        # Player Heal
        elif answer.lower() in ('heal','h'):
            self.healtimes += 1
            # Test how many times healed in a fight
            if self.healtimes >= 2:
                print ("You can only heal once during a fight.")
            else:
                self.playerHeal()
        else:
            print("You slip...")

    # Heal Player Routine
    def playerHeal(self):
        if self.healtimes >= 2:
            print ("You can only heal twice between fights.\n")
        else:    
            if self.biocort >= 1:
                self.healtimes += 1
                self.biocort -= 1
                iHeal = int(random.randint(1, 4)*5)
                self.health += iHeal
                print("You hit yourself with a biocort, healing for {0} points of damage.".format(iHeal))
                if self.health >= self.maxhealth:
                    self.health = self.maxhealth
                print("Your health is now {0}.\n".format(self.health))
            else:
                print("You don't have any biocort.\n")

    # Draw Stats Routine
    def drawStats(self):
        print ("""----------------
Race: Human
Class: Enforcer
Level: {0.level}
Experience: {1.exp}
Health: {2.maxhealth}/{3.health}
Biocort: {4.biocort}
""".format(self, self, self, self, self))
        if self.defense == 35:
            print ("Armor: Flack Jacket (Val: 35)")
        else:
            print ("Armor: Bullet Proof Veset (Val: 50)")    
        if self.weapontype == 1:
            print ("Weapon: Laser Pistol (Dmg: 1d30 - 3 SEU per shot)")
        else:
            print ("Weapon: Laser Rifle (Dmg: 1d50 - 5 SEU per shot)")
        print("""SEUs: {0.seutotal}  /  Clips: {1.clips}
Credits: {2.cash}
----------------
""".format(self, self, self))

    # Player Status Routine    
    def playerStatus(self):
        flag = 1
        inStatus = 1
        self.drawStats()
        print("""What do you want to do?

1 - Stats
2 - Heal
3 - Reload
4 - Back
""")
        # Player Input
        while (inStatus):
            while (flag):
                tempInput = input("> ")
                if tempInput == "1":
                    flag = 0
                elif tempInput == "2":
                    flag = 0
                elif tempInput == "3":
                    flag = 0
                elif tempInput == "4":
                    flag = 0
                    inStatus = 0
                else:
                    self.drawStats()
                    print ("""Please choose a number below.

1 - Stats
2 - Heal
3 - Reload
4 - Back
""")
            # Print Player Stats
            if tempInput == "1":
                flag = 1
                self.drawStats()
                print ("""What do you want to do?

1 - Stats
2 - Heal
3 - Reload
4 - Back
""")
            # Heal Player
            elif tempInput == "2":
                flag = 1
                self.playerHeal()
            # Reload Weapon
            elif tempInput == "3":
                flag = 1
                self.playerReload()

    # Reload Routine
    def playerReload(self):
        if self.clips == 0:
            print("You don't have any ammo...\n")
        else:
            self.seutotal = 10
            self.clips -= 1
            print("You reload your weapon.\n")
