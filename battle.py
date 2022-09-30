import random
from dmg_calc import dmg_calc

choices = ["up high", "in the middle", "down low"]

def player_atk(monster,hp2, atk2, dfens2, str1, weapon1, armor2, def2):
    if atk2 not in choices:
        print(
            f"Sorry I didn't understand you. You are attacking the {monster}. You may attack up high, in the middle or down low. Choose where u want to attack: "
        )
    else:
        dmg2 = dmg_calc(atk2, dfens2, str1, weapon1, armor2, def2)
        hp2 = hp2 - dmg2
        if hp2 <= 0:
            hp2 = 0
        print(
                f"You attacked the {monster} {atk2}.  The {monster} defended {dfens2}. You hit the {monster} and did {dmg2} damage. The {monster} now has {hp2} health remaining"
            )
    return hp2


def enemy_atk(monster,hp1, atk1, dfens1, str2, weapon2, armor1, def1):
    if dfens1 not in choices:
        print("Sorry I didn't understand you. The {monster} is attacking you.")
    else:
        dmg1 = dmg_calc(atk1, dfens1, str2, weapon2, armor1, def1)
        hp1 = hp1 - dmg1
        if hp1 <= 0:
            hp1 = 0
        print(
            f"The {monster} attacked you {atk1}.  You defended {dfens1}. The {monster} hit you and did {dmg1} damage. You now have {hp1} health remaining"
        )
    return hp1
