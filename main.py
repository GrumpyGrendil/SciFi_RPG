# SciFi_RPG
# Simple Text-Based RPG, loosely based on Star Frontiers.
# Mostly random grinding with leveling and a shop.
# Written In Python 3.7

import random
from player import Player
from enemy import Enemy
from locations import *
from battle import *
        
def endGame(kills):
    print("""
*** Game Over ***""")
    if kills == 1:
        print ("You killed {0}  mob.".format(kills))
    else:
        print ("You killed {0}  mobs.".format(kills))
   
# Start of Game
new_enemy = newEnemy()
showIntro(new_enemy)
tempCash = int(random.randint(1, 25)+75)+200
# Creates New Player
# (block, health, maxhealth, defense, kills, biocort, cash, exp, seu, seutotal, weapondmg, weapontype, clips, healtimes, level, nextlevel):
# weapontype: 1 = pistol / 2 = rifle
new_player = Player(0,100, 100, 35, 0, 2, tempCash, 0, 3, 10, "laser pistol", 30, 1, 5, 0, 1, 100)
battle(new_player, new_enemy)
if new_player.health <= 0:
    endGame(new_player.kills)
    gameState = 0
else:
    new_player.kills += 1
    new_player.healtimes = 0
    gameState = 1

oldInput = "1"

# Game Loop
while gameState:
    # After Returning To Main Game Loop, Print Out One Of These
    if oldInput == "1":
        print ("Dusting yourself off, you decide where to go.")
    elif oldInput == "2":
        print ("Leaving the hotel, you decide where to go.")
    elif oldInput == "3":
        print ("Leaving the shop, you decide where to go.")
    elif oldInput == "4":
        print ("Where do you want to go?")
    else:
        print ("Please choose a number below.")
    print ("""
1 - Explore Station
2 - Cheap Hotel
3 - Shop

4 - Status
""")
    tempInput = input("> ")
    oldInput = tempInput
    # Player Explores The Station    
    if tempInput == "1":
        tempLocation = int(random.randint(1, 100))
        if tempLocation <= 25:
            spaceBar(new_player)
        elif tempLocation <= 50:
            restaurant(new_player)
        elif tempLocation <= 75:
            corridor(new_player)
        else:
            spacePort(new_player)
        # Check To See If Player Is Dead & End Game
        if new_player.health <= 0:
            endGame(new_player.kills)
            gameState = 0
        else:
            new_player.kills += 1
            new_player.healtimes = 0
    # Player Goes To Cheap Hotel
    elif tempInput == "2":
        cheapHotel(new_player)
    # Player Goes To The Shop
    elif tempInput == "3":
        spaceShop(new_player)
    # Player Goes To Status Section
    elif tempInput == "4":
        new_player.playerStatus()
