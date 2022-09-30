import random
from chrcter import avatar, stats
from database import weapons
from database import armors
from database import monsters
from dmg_calc import dmg_calc
health,gold,stats=avatar()
monster="Goblin"
hp1=health
str1=stats["Strength"]
def1=0
dex1=stats["Dexterity"]
hp2 = monsters[monster]["HP"]
str2= monsters[monster]["Strength"]
def2=monsters[monster]["Defense"]
dex2=monsters[monster]["Dexterity"]
choices = ["up high", "in the middle" ,"down low"]
turn=0
print(f"Welcome to the dungeon!There is a {monster} here.")

armor = str(input("Enter Armor:"))
weapon = str(input("Enter Weapon:"))
while hp1 > 0 and hp2 > 0:
    if dex1>dex2:
        turn=1
    else:
        turn=0
    if turn%2==0:
        
        atk1 = random.choice(choices)
        dfens1 = input(" It is attacking you. You may defend up high, in the middle or down low. Choose where u want to defend: ")
        if dfens1 not in choices:
            print("Sorry I didn't understand you. The {monster} is attacking you.")
        else:
            dmg1 = dmg_calc(atk1,dfens1,str2,weapon,armor,def1)
            hp1 = hp1 - dmg1
            if hp1 <= 0:
                hp1 =0
            print(f"The {monster} attacked you {atk1}.  You defended {dfens1}. The {monster} hit you and did {dmg1} damage. You now have {hp1} health remaining")
            if hp1 == 0:   
                print(f"Oh no! The {monster} has killed you. The {monster} searched your dead body and took all yours belonging")   
                break  
        turn+=1
    else:
        dfens2 = random.choice(choices)
        atk2 = input(f"It is your turn. You are attacking the {monster}. You may attack up high, in the middle or down low. Choose where u want to attack: ")

        if atk2 not in choices:
            print(f"Sorry I didn't understand you. You are attacking the {monster}. You may attack up high, in the middle or down low. Choose where u want to attack: ")
        else:
            dmg2 = dmg_calc(atk2,dfens2,str1,weapon,armor,def2)
            hp2 = hp2 - dmg2
            if hp2 <= 0:
                hp2 =0
            print(f"You attacked the {monster} {atk2}.  The {monster} defended {dfens2}. You hit the {monster} and did {dmg2} damage. The {monster} now has {hp2} health remaining")
            if hp2 == 0:
                print(f"Bazinga! You have killed the {monster}. You searched it dead body and got 50 golden coins")
        turn+=1
