import random

# Battle Routine
def battle(player, enemy):
    player.healtimes = 0
    print ("The {0.name} gets ready to attack...".format(enemy))
    # Combat Loop
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        print("The health of the {0.name} is now {0.health}.".format(enemy))
        # Special Cases
        if enemy.health <= 0:
            break
        # Blocking Output
        if player.block == 1:
            print("The {0.name} misses...".format(enemy))
            player.block = 0
        elif player.block == 2:
            print("The {0.name} hits you...".format(enemy))
            player.block = 0
        else:
            enemy.attack(player)
        # Print Player Health
        print("""Your health is now {0.health}.
""".format(player))

    # Player Wins Fight
    if player.health > 0:
        # Test If Player Gets Cash, 10% Failure
        tempAward = int(random.randint(1, 100))
        if tempAward >= 90:
            print("You killed the {0.name}, but found nothing on him.".format(enemy))
        else:
            # Give Cash 1d100+100
            tempCash = int(random.randint(1, 100)+100)
            player.cash += tempCash
            print("You killed the {0.name}, finding {1} credits on him.".format(enemy, tempCash))
        # Test If The Character Is Awarded Any Biocort And Apply It
        # Skip If The Player Found Nothing
        if tempAward >= 90:
            tempRandom = 100
        else:
            tempRandom = int(random.randint(1, 100))
        if tempRandom <= 10:
            tempBiocort = int(random.randint(1, 3))
            player.biocort += tempBiocort
            print("You also find {0} biocort on him.".format(tempBiocort))
        # Award Experience
        player.exp += enemy.exp
        # Check If Player Levels Up
        if player.exp >= player.nextlevel:
            # Level Up:
            # Reset Experience
            player.exp = 0
            # Increase The Amonut Of Experience Needed To Level
            player.nextlevel = int(player.nextlevel * 2.5)
            # Increase Max Health - Award Before Apply Level
            player.maxhealth += 10 * player.level
            # Increase Level
            player.level += 1
            print("After killing the {0.name}, you feel yourself becoming stronger!".format(enemy))
    #Mob Wins
    elif enemy.health > 0:
        print("The {0.name} killed you.".format(enemy))
