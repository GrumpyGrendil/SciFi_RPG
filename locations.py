import random
from enemy import Enemy
from battle import *

def yesNo():
    flag = 1
    # Player Input
    while (flag):
        tempInput = input("> ")
        if tempInput == "1":
            flag = 0
        elif tempInput == "2":
            flag = 0
        else:
            print ("""Please choose a number below.

1 - Yes
2 - No
""")            
    return tempInput

# New Enemy
# (name, strength, defense, health, exp)
def newEnemy():
    iRandom = int(random.randint(1, 4))
    if iRandom == 1:                
        return Enemy("Star Devil Pirate", 15, 30, 25, 15)
    elif iRandom == 2:
        return Enemy("Yazirian Mercenary", 15, 30, 35, 15)
    elif iRandom == 3:
        return Enemy("Malthar Dralasite", 20, 35, 40, 20)
    else:
        return Enemy ("Vrusk Goon", 25, 40, 35, 30)    

#Print Intro
def showIntro(enemy):
    print("""
      Station 9
====================
A Star Frontiers RPG

Station 9.  A docking hub outside of the Inner Reach
that's a temporary home. You live out of a single berth.
Looking to make some extra money, you head down
to the local bar.

Location: Space Bar

You find the bar full of strange characters.  Stepping up to
the counter to get a drink, you run into a {0.name}
looking for a fight!
""".format(enemy))

# Space Bar
def spaceBar(player):
    new_enemy = newEnemy()
    print("""You head over to the Space Bar.

Location: Space Bar

Walking into the bar you find a fight going on. A {0.name}
pulls out a laser rifle and points it at you.
""".format(new_enemy))
    battle(player, new_enemy)

# Space Port
def spacePort(player):
    new_enemy = newEnemy()
    print("""You head down to the Space Port.

Location: Space Port

\"What do you think you're doing here?\" asks a {0.name}
as he pulls out a laser rifle.
""".format(new_enemy))
    battle(player, new_enemy)

# Local Restaurant
def restaurant(player):
    new_enemy = newEnemy()
    print("""You head up to a local restaurant.

Location: Restaurant

A bunch of species clamor for deals.  Stepping in,
you bump into one.  \"You're not getting out of here
alive.\" says a {0.name}, pulling out
a force knife.
""".format(new_enemy))
    battle(player, new_enemy)

# Corridor
def corridor(player):
    new_enemy = newEnemy()
    print("""As you head back to the bar, you notice someone
following you.

Location: Corridor

You stop and turn, asking him what he is doing?
\"I'm robbing you, but you'll probably end up dead,\"
says the {0.name}, Needler in his hand.
""".format(new_enemy))
    battle(player, new_enemy)

# Shop
def spaceShop(player):
    flag = 1
    inStore = 1
    print ("""You go over to the local shop.

Location: Shop

You walk in on a hookah smoking Osakar. \"How can I
help you?\" he asks.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
    # Player Input
    while (inStore):
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
            elif tempInput == "5":
                flag = 0
                inStore = 0
            else:
                print ("""Please choose a number below.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
        # Buy Biocort            
        if tempInput == "1":
            print ("""\"That will be 10 credits,\" says the Osakar, \"do you want to pay?\"

1 - Yes
2 - No
""")
            flag = 1
            tempQuestion = yesNo()
            if tempQuestion == "1":
                if player.cash >= 10:
                    player.cash -= 10
                    player.biocort += 1
                    print ("""\"Thank you for the purchase,\" says the Osakar,
\"Do you need anything else?\"

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
                else:
                    print ("""\"Sorry, it looks like you don't have the credits,\"
the Osakar says as he packs another pipe, \"so how can I help you?\"

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
            if tempQuestion == "2":
                print ("""\"Maybe you'll buy something else,\" says the Osakar
as he takes a slow draw off his hookah.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
        # Buy Clips
        if tempInput == "2":
            print ("""\"That will be 50 credits,\" says the Osakar, \"do you want to pay?\"

1 - Yes
2 - No
""")
            flag = 1
            tempQuestion = yesNo()
            if tempQuestion == "1":
                if player.cash >= 50:
                    player.cash -= 50
                    player.clips += 1
                    print ("""\"Thank you for the purchase,\" says the Osakar,
\"Do you need anything else?\"

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
                else:
                    print ("""\"Sorry, it looks like you don't have the credits,\"
the Osakar says as he packs another pipe, \"so how can I help you?\"

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
            if tempQuestion == "2":
                print ("""\"Maybe you'll buy something else,\" says the Osakar
as he takes a slow draw off his hookah.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
        # Buy Weapon
        if tempInput == "3":
            flag = 1
            if player.weapontype == 2:
                print ("""\"Sorry I don't have any upgrades for you,\" the Osakar apologizes
as he taps out his bowl.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
            else:
                print ("""\"I have a fine Laser Rifle here. That'll be 1000 credits with
the turn in\" says the Osakar, \"do you want to pay?\"

1 - Yes
2 - No
""")
                tempQuestion = yesNo()
                if tempQuestion == "1":
                    if player.cash >= 1000:
                        player.cash -= 1000
                        player.weapon = "laser rifle"
                        player.weapontype = 2
                        player.seu = 5
                        player.seutotal = 0
                        player.weapondmg = 50
                        print ("""\"Look at that, a fine weapon indeed.\" states the Osakar,
\"Do you need anything else?\"

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
                    else:
                        print ("""\"Sorry, it looks like you don't have the credits,\" the Osakar says
as he packs another bowl, \"so how can I help you?\"

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
                if tempQuestion == "2":
                    print ("""\"Maybe you'll buy something else,\" says the Osakar
as he takes a slow draw off his hookah.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
        # Buy Armor
        if tempInput == "4":
            flag = 1
            if player.defense == 50:
                print ("""\"Sorry I don't have any upgrades for you,\" the Osakar apologizes
as he taps out his bowl.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
            else:
                print ("""\"I have this Bullet Proof Vest here. That'll be 500 credits with
the turn in\" says the Osakar, \"do you want to pay?\"

1 - Yes
2 - No
""")
                tempQuestion = yesNo()
                if tempQuestion == "1":
                    if player.cash >= 500:
                        player.cash -= 500
                        player.defense = 50
                        print ("""\"There you go, that'll protect you for sure,\" the Osakar says,
handing you the Armor.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
                    else:
                        print ("""\"Sorry, it looks like you don't have the credits,\" the Osakar says
as he packs another bowl, \"so how can I help you?\"

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")
                if tempQuestion == "2":
                    print ("""\"Maybe you'll buy something else,\" says the Osakar
as he takes a slow draw off his hookah.

1 - Buy Biocort
2 - Buy Clip
3 - Buy Weapon
4 - Buy Armor
5 - Leave Shop
""")

# Cheap Hotel
def cheapHotel(player):
    inHotel = 1
    print ("""You go over to Cheap Hotel, taking a shortcut through a
back alley.

Location: Cheap Hotel

A Yazirian Broker sits behind the desk, smoking a Yiheyuan.
\"If you want to sleep here it will cost 200 credits.\"

1 - Yes
2 - No
""")
    while (inHotel):
        tempInput = input("> ")
        if tempInput == "1":
            inHotel = 0
        elif tempInput == "2":
            inHotel = 0
        else:
            print ("""Please choose a number below.

1 - Yes
2 - No
""")
    if tempInput == "1":
        if player.cash >= 200:
            player.cash -= 200
            player.health = player.maxhealth
            print("""\"Thanks for the cash friend,\" he says with a smile,
\"Usual room, you know the place.\"

After crawling into your coffin, you rest up for a few hours
tending to your wounds.
""")
        else:
            print("""\"Looks like you don't have the cash,\" says the Yazirian
scratching his head.
""")
    elif tempInput == "2":
        print("""\"Come back when you have the cred,\" the Yazirian taunts.
""")
