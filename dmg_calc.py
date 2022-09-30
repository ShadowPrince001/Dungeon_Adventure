import random
from database import weapons
from database import armors



def dmg_calc(atk, defens, strnth, weapn, armr,defnse):
    if atk != defens:
        dmg = (
            2
            * int(random.randrange(weapons[weapn]["WC"][0], (weapons[weapn]["WC"][1])))
            + strnth
            - armors[armr]["AC"]
            -defnse
        )
    else:
        dmg = (
            int(random.randrange(weapons[weapn]["WC"][0], (weapons[weapn]["WC"][1])))
            + strnth
            - armors[armr]["AC"]
            -defnse
        )
    if dmg<0:
        dmg=0
    return(dmg)
