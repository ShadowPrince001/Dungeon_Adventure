import random
import sys
import math

from chrcter import avatar, stats
from database import weapons, armors, potions, monsters
from dmg_calc import dmg_calc, crit
from shops import inventory
from battle import player_atk, enemy_atk


choices = ["up high", "in the middle", "down low"]
floor = 0
actions = [
    "Open shop",
    "Buy supplies",
    "Check stats",
    "Equip",
    "Check Inventory",
    "Scout floor",
    "Analyse monster",
    "Climb tower",
]


def shop():
    global gold
    global stats
    while True:
        if stats["Charisma"] > 18:
            print(
                f"The shop keeper fell for your charisma and wants to give you a 10% discount on all products"
            )
        item = input("What would you like to buy?\n Armor,Weapon,Potion or Leave\n")
        if item == "Armor":
            armr = str(input("Enter Armor:"))
            if armr not in armors.keys():
                print("There is no such armor. Please choose again.")
            elif armors[armr]["Cost"] > gold:
                print("You do not have enough gold to purchase the item")
            else:
                inventory.append(armr)
                if stats["Charisma"] > 18:
                    armors[armr]["Cost"] *= 0.9
                gold -= armors[armr]["Cost"]
                print(f"You bought a {armr} ")
        elif item == "Weapon":
            wpn = str(input("Enter Weapon:"))
            if wpn not in weapons.keys():
                print("There is no such weapon. Please choose again.")
            elif weapons[wpn]["Cost"] > gold:
                print("You do not have enough gold to purchase the item")
            else:
                inventory.append(wpn)
                if stats["Charisma"] > 18:
                    weapons[wpn]["Cost"] *= 0.9
                gold -= weapons[wpn]["Cost"]
                print(f"You bought a {wpn} ")
        elif item == "Potion":
            ptn = str(input("Enter potion:"))
            if ptn not in potions.keys():
                print("There is no such potion. Please choose again.")
            elif potions[ptn]["Cost"] > gold:
                print("You do not have enough gold to purchase the item")
            else:
                inventory.append(ptn)
                if stats["Charisma"] > 18:
                    potions[ptn]["Cost"] *= 0.9
                gold -= potions[ptn]["Cost"]
                print(f"You bought a {ptn} ")
        elif item == "Leave":
            print("You left the shop")
            break
        else:
            print("There is no such item.")


def equip():
    curr_armor = "No Armor"
    curr_weapon = "Unarmed"
    curr_potion = "Potion of Nothingness"
    while True:
        item = input(
            "What would you like to equip or use?\n Armor,Weapon,Potion or Leave\n"
        )
        if item == "Armor":
            curr_armor = str(input("Enter Armor:"))
            if curr_armor not in inventory:
                print("You have no such armor. Please choose again.")
            else:
                print(f"You equipped your {curr_armor}")
        elif item == "Weapon":
            curr_weapon = str(input("Enter Weapon:"))
            if curr_weapon not in inventory:
                print("You have no such weapon. Please choose again.")
            else:
                print(f"You equipped your {curr_weapon} ")
        elif item == "Potion":
            curr_potion = str(input("Enter potion:"))
            if curr_potion not in inventory:
                print("You have no such potion. Please choose again.")
        elif item == "Leave":
            break
        else:
            print("There is no such item.")

    return curr_armor, curr_weapon, curr_potion


print(
    f"Welcome to the tower!Your aim is to kill the dragon that is terrorising the nearby villages. But for that you need to embark on a journey where you defeat countless monsters and try to stay alive.There are 15 levels in this tower"
)
action = ""
health, gold, stats = avatar()
hp1 = health
str1 = stats["Strength"]
def1 = (stats["Strength"] + stats["Constitution"]) / 2
dex1 = stats["Dexterity"]
armor1 = "No Armor"
weapon1 = "Unarmed"
while hp1 > 0:
    print("What would you like to do?\nSome actions you can do are:")
    for a in actions:
        print(a, end="\n")
    action = str(input("\n"))
    if action == actions[0]:
        print("\nThe list of armors is\n")
        for keys, values in armors.items():
            print(keys, " : ", values)
        print("\nThe list of weapons is\n")
        for keys, values in weapons.items():
            print(keys, " : ", values)
        print("\nThe list of potions is\n")
        for keys, values in potions.items():
            print(keys, " : ", values)
    elif action == actions[1]:
        shop()
    elif action == actions[2]:
        for key, value in stats.items():
            print(key, " : ", value)
        print("Your remaining health is", hp1)
        print(f"You have {gold} golden coins.")
        print(f"Your current weapons is {weapon1}")
        print(f"Your current armor is {armor1}")
    elif action == actions[3]:
        armor1, weapon1, potion1 = equip()
        heal = int(potions[potion1]["Recover"])
        hp1 += heal
        if hp1 > health:
            hp1 = health
        if heal != 0:
            print(
                f"You drank a {potion1} and healed {heal} HP and now currently have {health} HP."
            )

    elif action == actions[4]:
        print(inventory, sep="\n")
    elif action == actions[5]:
        if stats["Perception"] >= 15:
            for m in monsters.keys():
                if monsters[m]["Floor"] == floor + 1:
                    print(f"The monster in the next floor is {m}.")
        else:
            print(
                "You failed to scout the next floor since your perception is too low."
            )
    elif action == actions[6]:
        if stats["Intellect"] >= 15:
            mnster = str(input("Enter the monster you would like to analyse: "))
            print(monsters[mnster])
        else:
            print("Your intellect is too low to analyse monsters.")
    elif action == actions[7]:
        turn = 0
        floor += 1
        if floor > 15:
            floor = 0
            print("You tried to climb further but instead you fell down.")
        for b in monsters.keys():
            if monsters[b]["Floor"] == floor:
                monster = b
        floor = monsters[monster]["Floor"]
        hp2 = monsters[monster]["HP"]
        str2 = monsters[monster]["Strength"]
        def2 = monsters[monster]["Defense"]
        dex2 = monsters[monster]["Dexterity"]
        weapon2 = monsters[monster]["Weapon"]
        armor2 = monsters[monster]["Armor"]
        gld_drp = int(
            random.randrange(
                monsters[monster]["Gold"][0], (monsters[monster]["Gold"][1])
            )
        )
        if stats["Luck"] >= 15:
            gld_drp *= 1.25
        print(f"You are in {floor} floor. There is a {monster} here.")
        if dex1 < dex2:
            turn += 1
        while hp1 > 0 and hp2 > 0:
            if turn % 2 == 1:
                atk1 = random.choice(choices)
                dfens1 = input(
                    "It is attacking you. You may defend up high, in the middle or down low. Choose where u want to defend: "
                )
                if dfens1 not in choices:
                    print("Sorry I didn't understand you.")
                else:
                    turn += 1
                    hp1 = enemy_atk(
                        monster, hp1, atk1, dfens1, str2, weapon2, armor1, def1
                    )
                if hp1 == 0:
                    print(
                        f"Oh no! The {monster} has killed you. The {monster} searched your dead body and took all yours belonging."
                    )
                    break
                    sys.exit(
                        "Adventurer, your journey ends here. The dragon slaughtered all the helpless villagers after your death. Better luck in your next try"
                    )

            else:

                dfens2 = random.choice(choices)
                atk2 = input(
                    f"It is your turn. You are attacking the {monster}. You may attack up high, in the middle or down low. Choose where u want to attack: "
                )
                if atk2 not in choices:
                    print("Sorry I didn't understand you. ")
                else:
                    turn += 1
                    crit(stats["Luck"])
                    hp2 = player_atk(
                        monster, hp2, atk2, dfens2, str1, weapon1, armor2, def2
                    )
                    if hp2 == 0 and floor == 0:
                        print(
                            f"Congratulions! You have kille the {monster}. It seems that Azazel was the ruler and creator of the tower. With his death the tower starts to crumble to dust and you manage to barely escape. The villages hail you as their hero and shower you with praise."
                        )
                        break
                        sys.exit("Congratulions you have finished the game. Thank you for playing it.")
                    if hp2 == 0:
                        print(
                            f"You have killed the {monster}. You searched it dead body and got {gld_drp} golden coins"
                        )
                        gold += gld_drp
                        break

    else:
        print("Sorry you cannot do that.")
