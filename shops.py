from database import weapons
from database import armors


def shop():
    print("\nThe list of armors is\n")
    for keys, values in armors.items():
        print(keys, " : ", values)
    print("\nThe list of weapons is\n")
    for keys, values in weapons.items():
        print(keys, " : ", values)
    while True:
        armor1 = str(input("Enter Armor:"))
        if armor1 not in armors.keys():
            print("There is no such armor. Please choose again.")
        else:
            break
    while True:
        weapon1 = str(input("Enter Weapon:"))
        if weapon1 not in weapons.keys():
            print("There is no such weapon. Please choose again.")
        else:
            break

    return armor1, weapon1


shop()
