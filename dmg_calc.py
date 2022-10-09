import random
from database import weapons
from database import armors

crit_dmg = 1


def crit(luck):
    global crit_dmg
    if luck >= 21:
        num = random.randint(4, 6)
    elif luck >= 15:
        num = random.randint(3, 7)
    else:
        num = random.randint(1, 10)
    if num == 5:
        crit_dmg = 1.5
    return crit_dmg


def dmg_calc(atk, defens, strnth, weapn, armr, defnse):
    if atk != defens:
        dmg = round(
            crit_dmg
            * (
                2
                * (
                    int(
                        random.randrange(
                            weapons[weapn]["WC"][0], (weapons[weapn]["WC"][1])
                        )
                    )
                    + strnth
                    - armors[armr]["AC"]
                    - defnse
                )
            )
        )
    else:
        dmg = (
            int(random.randrange(weapons[weapn]["WC"][0], (weapons[weapn]["WC"][1])))
            + strnth
            - armors[armr]["AC"]
            - defnse
        )
    if dmg < 0:
        dmg = 0
    return dmg
