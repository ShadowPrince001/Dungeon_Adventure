stats_list = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intellect",
    "Luck",
    "Charisma",
    "Perception",
]
gld = 0


def train(gold, trn):
    while True:

        stat = str(input(f"What attribute would you like to train?\n"))
        if stat in stats_list:
            gld = 50 * (1 + trn)
            if gld > gold:
                print("You do not have enough gold to train.")
                break
            else:
                return stat, gld
        else:
            print(
                "That is not an attribute. The attributes you can choose are ",
                stats_list,
            )
