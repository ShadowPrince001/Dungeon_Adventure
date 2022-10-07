import random
import math

stats = {
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intellect": 0,
    "Luck": 0,
    "Charisma": 0,
    "Perception": 0,
}

stats_list = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intellect",
    "Luck",
    "Charisma",
    "Perception",
]


def avatar():
    name = str(input("Lets start your journey,Adventurer. What is your name?\n"))
    print(name, ",Lets start building your character")
    print(
        "The attributes you can choose are ",
        stats_list,
    )
    for n in range(7):
        rolls = []
        stat = 0
        print("You rolled a ")
        for a in range(4):
            roll = random.randint(1, 6)
            stat += roll
            rolls.append(roll)
        print(rolls)
        print("So, your final value is ", stat)
        b = 0
        while b == 0:
            try:
                x = str(
                    input(
                        "What attribute will you like to assign your value of "
                        + str(stat)
                        + " to?\n"
                    )
                )
                if stats[x] == 0:
                    b += 1
                else:
                    print(
                        "The attributes you can choose are ",
                        stats_list,
                    )

            except KeyError:
                print(
                    "That is not an attribute. The attributes you can choose are ",
                    stats_list,
                )
                continue
        stats[x] = stat
        stats_list.remove(x)
        print("Your current stats are\n")
        for key, value in stats.items():
            print(key, " : ", value)
    print("Your character is almost ready.")
    if stats["Luck"] >= 21:
        health = 3 * (int(stats["Constitution"]) + (random.randint(15, 20)))
    elif stats["Luck"] >= 15:
        health = 3 * (int(stats["Constitution"]) + (random.randint(10, 20)))
    else:
        health = 3 * (int(stats["Constitution"]) + (random.randint(1, 20)))
    print("Your starting health is", health)
    print("Rolling for your starting gold. You rolled a ")
    rolls = []
    gold = 0
    x = 5 * round(((int(stats["Charisma"])) - 12) / 3)
    for n in range(20 + x):
        if stats["Luck"] >= 21:
            roll = random.randint(5, 6)
        elif stats["Luck"] >= 15:
            roll = random.randint(3, 6)
        else:
            roll = random.randint(1, 6)
        rolls.append(roll)
        gold += roll
    for i in rolls:
        print(rolls[i], end=" ")
    print("\nYour starting gold is", gold)
    return health, gold, stats
