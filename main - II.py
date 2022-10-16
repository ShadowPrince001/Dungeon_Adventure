import random
import sys
import math
import pickle
import os

from chrcter import avatar, stats
import enchant
from database import weapons, armors, potions, monsters
from dmg_calc import dmg_calc, crit
from battle import player_atk, enemy_atk
from train import train

try:
    with open("armor1.dat", "rb") as fin:
        inventory=pickle.load(fin)
except:
    inventory = ["Unarmed", "No Armor"]
    with open("inventory.dat", "wb") as fout:
        pickle.dump(inventory,fout)
choices = ["up high", "in the middle", "down low"]
trained = 0
enchnt=0
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
    "Enchant",
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
            with open("inventory.dat", "wb") as fout:
                pickle.dump(inventory,fout)
            break
        else:
            print("There is no such item.")


def equip():
    global curr_armor, curr_weapon
    with open("inventory.dat", "rb") as fin:
        inventory=pickle.load(fin)
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
    with open("inventory.dat", "rb") as fin:
        inventory=pickle.load(fin)
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
                with open("inventory.dat", "wb") as fout:
                    pickle.dump(inventory,fout)
        elif curr_potion not in inventory:
            print("You have no such potion. Please choose again.")
        else:
            print("There is no such potion.")
        return curr_potion


def sell():
    global gold
    global armor1, weapon1, potion1
    with open("inventory.dat", "rb") as fin:
        inventory=pickle.load(fin)
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
                with open("inventory.dat", "wb") as fout:
                    pickle.dump(inventory,fout)
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
                with open("inventory.dat", "wb") as fout:
                    pickle.dump(inventory,fout)
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
                with open("inventory.dat", "wb") as fout:
                    pickle.dump(inventory,fout)
                gold += gld
        elif item == "Leave":
            break
        else:
            print("There is no such item.")


print(
    f"Welcome to the Tower of Trials!Your aim is to kill the monsters that are terrorising the nearby villages. But for that you need to embark on a journey where you defeat countless monsters and try to stay alive.There are 15 levels in this tower"
)
action = ""
try:
    health,gold,stats=avatar()
except:
    pass
with open("stats.dat", "rb") as fin:
    stats=pickle.load(fin)
with open("gold.dat", "rb") as fin:
    gold=int(pickle.load(fin))
with open("health.dat", "rb") as fin:
    health=int(pickle.load(fin))
hp1 = int(health)
armor1 = "No Armor"
weapon1 = "Unarmed"
while hp1 > 0:
    try:
        with open("stats.dat", "wb") as fout:
            pickle.dump(stats,fout)
        with open("gold.dat", "wb") as fout:
            pickle.dump(gold,fout)
        with open("health.dat", "wb") as fout:
            pickle.dump(health,fout)
        with open("stats.dat", "rb") as fin:
            stats=pickle.load(fin)
        with open("gold.dat", "rb") as fin:
            gold=int(pickle.load(fin))
        with open("health.dat", "rb") as fin:
            health=int(pickle.load(fin))
        with open("trained.dat", "wb") as fout:
                pickle.dump(trained,fout)
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
            with open("armor1.dat", "wb") as fout:
                pickle.dump(armor1,fout)
            with open("weapon1.dat", "wb") as fout:
                pickle.dump(weapon1,fout)
            with open("weapon1.dat", "rb") as fin:
                weapon1=pickle.load(fin)
            with open("armor1.dat", "rb") as fin:
                armor1=pickle.load(fin)
        elif action == actions[4]:
            potion1 = use()
        elif action == actions[5]:
            
            with open("inventory.dat", "rb") as fin:
                inventory=pickle.load(fin)
            print(inventory)
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
            try:
                with open("floor.dat", "rb") as fin:
                    floor=int(pickle.load(fin))
            except:
                floor=0
                with open("floor.dat", "wb") as fout:
                    pickle.dump(floor,fout)
            floor += 1
            for b in monsters.keys():
                if monsters[b]["Floor"] == floor:
                    monster = b
            if floor == 16:
                print(
                        "It seems you have come across a hidden floor which didn't exist before."
                    )
            floor = monsters[monster]["Floor"]
            with open("floor.dat", "wb") as fout:
                pickle.dump(floor,fout)
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
                    if hp1 == 0 and floor==16:
                        print(
                            f"Oh no!{monster} has killed you.{monster} searched your dead body and took all yours belonging."
                        )
                        os.remove("stats.dat")
                        os.remove("gold.dat")
                        os.remove("health.dat")
                        os.remove("floor.dat")
                        os.remove("inventory.dat")
                        os.remove("trained.dat")
                        os.remove("armor1.dat")
                        os.remove("weapon1.dat")
                        sys.exit(
                            "Adventurer, your journey ends here.You managed to save the villagers but could not defeat the creator of the tower. Better luck in your next try"
                        )
                    elif hp1 == 0:
                        print(
                            f"Oh no! The {monster} has killed you. The {monster} searched your dead body and took all yours belonging."
                        )
                        os.remove("stats.dat")
                        os.remove("gold.dat")
                        os.remove("health.dat")
                        os.remove("floor.dat")
                        os.remove("inventory.dat")
                        os.remove("trained.dat")
                        os.remove("armor1.dat")
                        os.remove("weapon1.dat")
                        sys.exit(
                            "Adventurer, your journey ends here. The monsters escaped and slaughtered all the helpless villagers after your death. Better luck in your next try"
                        )
                elif turn == 50:
                    print(
                        f"Both you and the {monster} are tired and decide to continue fighting next time. You descend into the previous floor"
                    )
                    floor -= 1
                    break
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
                            monster, hp2, atk2, dfens2, str1, weapon1, armor2, def2,enchant_item
                        )
                        if hp2 == 0 and floor == 16:
                            print(
                                f"Congratulations! You have killed the {monster}. It seems that Azazel was the ruler and creator of the tower. With his death the tower starts to crumble to dust and you manage to barely escape. You have succesfully stopped the threat of the tower once and for all."
                            )
                            break
                            sys.exit(
                                "Congratulions you have finished the game. Thank you for playing it."
                            )
                        if hp2 == 0 and floor == 15:
                            print(
                                f"Congratulations! You have killed the {monster}. With the death of Dragon King all the monsters fall into a deep slumber. They will probably not attack the villages in the near future. The villagers hail you as their hero and shower you with praise."
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
            stat, gld, stat_pt = train(gold, trained)
            gold -= gld
            try:
                with open("trained.dat", "rb") as fin:
                    trained=pickle.load(fin)
            except:
                trained=0
                with open("trained.dat", "wb") as fout:
                    pickle.dump(trained,fout)
            trained += 1
            stats[stat] += stat_pt
            if stat_pt != 0:
                print(
                    f"You paid {gld} coins to train your {stat}. Your {stat} is now {stats[stat]}"
                )
                if stat == "Constitution":
                    hp1 += 3
                    health += 3
                    print(
                        f"Your total health increased by 3 HP. You currently have {hp1}/{health}HP"
                    )
        elif action == actions[11]:
            gld,enchant_item = enchant(gold)
            gold -= gld
            try:
                with open("enchant.dat", "rb") as fin:
                    enchant_item=pickle.load(fin)
            except:
                with open("enchant.dat", "wb") as fout:
                    pickle.dump(enchant_item,fout)
        elif action == actions[12]:
            sys.exit(
                "You have decided to quit your adventure for now. I hope you good luck in your next try."
            )

        else:
            print("Sorry you cannot do that.")
    except:
        continue
    
