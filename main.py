import random
from chrcter import avatar, stats
from database import weapons
from database import armors
from database import monsters
from dmg_calc import dmg_calc
from shops import shop
from battle import player_atk, enemy_atk

health, gold, stats = avatar()
monster = "Goblin"
hp1 = health
str1 = stats["Strength"]
def1 = 10
dex1 = stats["Dexterity"]
hp2 = monsters[monster]["HP"]
str2 = monsters[monster]["Strength"]
def2 = monsters[monster]["Defense"]
dex2 = monsters[monster]["Dexterity"]
weapon2 = monsters[monster]["Weapon"]
armor2 = monsters[monster]["Armor"]
choices = ["up high", "in the middle", "down low"]
turn = 0

armor1, weapon1 = shop()

print(f"Welcome to the dungeon!There is a {monster} here.")

if dex1 < dex2:
    turn += 1
while hp1 > 0 and hp2 > 0:
    if turn % 2 == 1:
        turn += 1
        atk1 = random.choice(choices)
        dfens1 = input(
            "It is attacking you. You may defend up high, in the middle or down low. Choose where u want to defend: "
        )

        hp1=enemy_atk(monster, hp1, atk1, dfens1, str2, weapon2, armor1, def1)
        if hp1 == 0:
            print(
                f"Oh no! The {monster} has killed you. The {monster} searched your dead body and took all yours belonging"
            )

    else:
        turn += 1

        dfens2 = random.choice(choices)
        atk2 = input(
            f"It is your turn. You are attacking the {monster}. You may attack up high, in the middle or down low. Choose where u want to attack: "
        )
        hp2=player_atk(monster, hp2, atk2, dfens2, str1, weapon1, armor2, def2)
        if hp2 == 0:
            print(
                f"Bazinga! You have killed the {monster}. You searched it dead body and got 50 golden coins"
            )
            break
