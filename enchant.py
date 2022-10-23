gld = 0


def enchant(gold):
    while True:

        enchant_item = str(input(f"Would you like to enchant your weapon or armor?\n"))
        if enchant_item == "Weapon" or "Armor":
            gld = int(500)
            if gld > gold:
                print("You do not have enough gold to enchant.")
                enchant_item = "null"
                gld = 0
                return enchant_item, gld
                break
            else:
                return enchant_item, gld
        else:
            print("You can only choose to enchant either weapon or armor.")
