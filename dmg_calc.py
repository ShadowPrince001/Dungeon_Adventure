import random
weapon={"Dagger":[7,10]}
armor={"Leather Armor":8}
def dmg_calc(atk,defens,strnth,weapn,armr,dfnse):
    if atk != defens:
        dmg=2*(random.randint(weapon[weapn][0],weapon[weapn][1]))+strnth-dfnse-armor[armr]
        print(dmg)
    else:
        dmg=(random.randint(weapon[weapn][0],weapon[weapn][1]))+strnth-dfnse-armor[armr]
        print(dmg)

dmg_calc(1,2,15,"Dagger","Leather Armor",13)
