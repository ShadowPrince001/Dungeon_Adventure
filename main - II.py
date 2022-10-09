import random
import sys
import math

from chrcter import avatar, stats
from database import weapons, armors, potions, monsters
from dmg_calc import dmg_calc, crit
from battle import player_atk, enemy_atk
from train import train

inventory = ["Unarmed", "No Armor"]
choices = ["up high", "in the middle", "down low"]
floor = 0
trained = 0
actions = [
    "Open shop",
    "Buy supplies",
    "Check stats",
    "Equip",
    "Use Potion",
    "Check Inventory",
    "Sell Items",
    "Scout floor",
    "Analyse monster",
    "Climb tower",
    "Train",
    "Quit game",
]
stats_list = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intellect",
    "Luck",
    "Charisma",
    "Perception",
]

curr_armor = "No Armor"
curr_weapon = "Unarmed"
curr_potion = "Potion of Nothingness"


def shop():
    global gold
    global stats
    if stats["Charisma"] >= 21:
        print(
            f"The shop keeper fell for your charisma and wants to give you a 25% discount on all products"
        )
    elif stats["Charisma"] >= 15:
        print(
            f"The shop keeper fell for your charisma and wants to give you a 10% discount on all products"
        )
    while True:

        item = input("What would you like to buy?\nArmor,Weapon,Potion or Leave\n")
        if item == "Armor":
            armr = str(input("Enter Armor:"))
            if armr not in armors.keys():
                print("There is no such armor. Please choose again.")
            else:
                if stats["Charisma"] >= 21:
                    armors[armr]["Cost"] *= 0.75
                elif stats["Charisma"] >= 15:
                    armors[armr]["Cost"] *= 0.9

                if armors[armr]["Cost"] > gold:
                    print("You do not have enough gold to purchase the item")
                else:
                    inventory.append(armr)
                    gold -= round(armors[armr]["Cost"])
                    print(f"You bought a {armr} for ", armors[armr]["Cost"], "gold.")
        elif item == "Weapon":
            wpn = str(input("Enter Weapon:"))
            if wpn not in weapons.keys():
                print("There is no such weapon. Please choose again.")
            else:
                if stats["Charisma"] >= 21:
                    weapons[wpn]["Cost"] *= 0.75
                elif stats["Charisma"] >= 15:
                    weapons[wpn]["Cost"] *= 0.9
                if weapons[wpn]["Cost"] > gold:
                    print("You do not have enough gold to purchase the item")
                else:
                    inventory.append(wpn)
                    gold -= round(weapons[wpn]["Cost"])
                    print(f"You bought a {wpn} for ", weapons[wpn]["Cost"], "gold.")
        elif item == "Potion":
            ptn = str(input("Enter potion:"))
            if ptn not in potions.keys():
                print("There is no such potion. Please choose again.")
            else:
                if stats["Charisma"] >= 21:
                    potions[ptn]["Cost"] *= 0.75
                elif stats["Charisma"] >= 15:
                    potions[ptn]["Cost"] *= 0.9

                if potions[ptn]["Cost"] > gold:
                    print("You do not have enough gold to purchase the item")
                else:
                    inventory.append(ptn)
                    gold -= round(potions[ptn]["Cost"])
                    print(f"You bought a {ptn} for ", potions[ptn]["Cost"], "gold.")
        elif item == "Leave":
            print("You left the shop")
            break
        else:
            print("There is no such item.")


def equip():
    global curr_armor, curr_weapon
    while True:
        item = input("What would you like to equip?\nArmor,Weapon or Leave\n")
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
        elif item == "Leave":
            break
        else:
            print("There is no such item.")

    return curr_armor, curr_weapon


def use():
    global hp1
    global curr_potion
    while True:
        curr_potion = input(f"What potion you like to use or Leave?\n")
        if curr_potion == "Leave":
            break
        elif curr_potion in inventory:
            heal = int(potions[curr_potion]["Recover"])
            hp1 += heal
            if hp1 > health:
                hp1 = health
            if heal != 0:
                print(
                    f"You drank a {curr_potion} and healed {heal} HP and now currently have {hp1}/{health} HP."
                )
                inventory.remove(curr_potion)
        elif curr_potion not in inventory:
            print("You have no such potion. Please choose again.")
        else:
            print("There is no such potion.")
        return curr_potion


def sell():
    global gold
    global armor1, weapon1, potion1
    while True:
        item = input("What would you like to sell?\nArmor,Weapon,Potion or Leave\n")
        if item == "Armor":
            armor1 = "No Armor"
            armr = str(input("Enter Armor:"))
            if armr not in inventory:
                print("You have no such armor. Please choose again.")
            else:
                gld = round(0.5 * (armors[armr]["Cost"]))
                print(f"You sold your {armr} for {gld}")
                inventory.remove(armr)
                gold += gld
        elif item == "Weapon":
            wpn = str(input("Enter Weapon:"))
            weapon1 = "Unarmed"
            if wpn not in inventory:
                print("You have no such weapon. Please choose again.")
            else:
                gld = round(0.5 * (weapons[wpn]["Cost"]))
                print(f"You sold your {wpn} for {gld} ")
                inventory.remove(wpn)
                gold += gld
        elif item == "Potion":
            ptn = str(input("Enter potion:"))
            potion1 = "Potion of Nothingness"
            if ptn not in inventory:
                print("You have no such potion. Please choose again.")
            else:
                gld = round(0.5 * (potions[ptn]["Cost"]))
                print(f"You sold your {ptn} ")
                inventory.remove(ptn)
                gold += gld
        elif item == "Leave":
            break
        else:
            print("There is no such item.")


print(
    f"Welcome to the tower!Your aim is to kill the monsters that are terrorising the nearby villages. But for that you need to embark on a journey where you defeat countless monsters and try to stay alive.There are 15 levels in this tower"
)
action = ""
health, gold, stats = avatar()
hp1 = health
armor1 = "No Armor"
weapon1 = "Unarmed"
while hp1 > 0:
    str1 = stats["Strength"]
    def1 = (stats["Strength"] + stats["Constitution"]) / 2
    dex1 = stats["Dexterity"]
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
        print(f"Your remaining health is {hp1}/{health} HP")
        print(f"You have {gold} golden coins.")
        print(f"Your current weapons is {weapon1}")
        print(f"Your current armor is {armor1}")
        print(f"You are currently in {floor} floor.")
    elif action == actions[3]:
        armor1, weapon1 = equip()
    elif action == actions[4]:
        potion1 = use()
    elif action == actions[5]:
        print(inventory, sep="\n")
    elif action == actions[6]:
        sell()
    elif action == actions[7]:
        if stats["Perception"] >= 15:
            for m in monsters.keys():
                if monsters[m]["Floor"] == floor + 1:
                    print(f"The monster in the next floor is {m}.")
        else:
            print(
                "You failed to scout the next floor since your perception is too low."
            )
    elif action == actions[8]:
        if stats["Intellect"] >= 15:
            mnster = str(input("Enter the monster you would like to analyse: "))
            print(monsters[mnster])
        else:
            print("Your intellect is too low to analyse monsters.")
    elif action == actions[9]:
        turn = 0
        floor += 1
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
        gld_drp = round(
            random.randrange(
                monsters[monster]["Gold"][0], (monsters[monster]["Gold"][1])
            )
        )
        if stats["Luck"] >= 21:
            gld_drp = round(gld_drp * 1.75)
        elif stats["Luck"] >= 15:
            gld_drp = round(gld_drp * 1.25)
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
                    sys.exit(
                        "Adventurer, your journey ends here. The monsters escaped and slaughtered all the helpless villagers after your death. Better luck in your next try"
                    )
            elif turn == 50:
                print(
                    f"Both you and the {monster} are tired and decide to continue fighting next time. You descend into the previous floor"
                )
                floor -= 1
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
                        sys.exit(
                            "Congratulions you have finished the game. Thank you for playing it."
                        )
                    if hp2 == 0:
                        print(
                            f"You have killed the {monster}. You searched it dead body and got {gld_drp} golden coins"
                        )
                        gold += gld_drp
                        while True:
                            try:
                                trn = str(
                                    input(
                                        f"You got a stat point.What attribute would you like to use it on? \n{stats_list}\n"
                                    )
                                )
                                stats[trn] += 1
                                print(
                                    f"You trained your {trn}. Your {trn} is {stats[trn]} now."
                                )
                                if trn == "Constitution":
                                    hp1 += 3
                                    health += 3
                                    print(
                                        f"Your total health increased by 3 HP. You currenlt have {hp1}/{health}HP"
                                    )
                                break
                            except KeyError:
                                print(
                                    f"That is not an attribute. The attributes you can choose are {stats_list} \n"
                                )
                                continue
                        break
    elif action == actions[10]:
        stat, gld = train(gold, trained)
        gold -= gld
        trained += 1
        stats[stat] += 1
        print(
            f"You paid {gld} coins to train your {stat}. Your {stat} is now {stats[stat]}"
        )
        if stat == "Constitution":
            hp1 += 3
            health += 3
            print(
                f"Your total health increased by 3 HP. You currenlt have {hp1}/{health}HP"
            )
    elif action == actions[11]:
        sys.exit(
            "You have decided to quit your adventure for now. I hope you good luck in your next try."
        )

    else:
        print("Sorry you cannot do that.")
