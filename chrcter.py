import random

stats={"Strength":0,
       "Dexterity":0,
       "Constitution":0,
       "Intelligence":0,
       "Wisdom":0,
       "Charisma":0,
       "Perception":0
       }

name=str(input("Welcome to Dungeon Adventure. I am the Dungeon Master. Adventurer, What is your name?\n"))
print(name,",Lets start building your character")
for n in range(7):
    stat=0
    print("You rolled a ")
    for a in range(4):
        roll=random.randint(1,6)
        stat+=roll
        print(roll)
    print("So, your final value is ",stat)
    b=0
    while b == 0:
        try:
            x=str(input("What attribute will you like to assign your value of "+str(stat)+" to?\n"))
            if stats[x] ==0:
                b +=1
        except KeyError:
            print("That is not an attribute. The attributes you have are",list(stats.keys()))
            continue
    stats[x]=stat
    print("Your current stats are\n")
    for key, value in stats.items():
        print(key, ' : ', value)

print("Your character is almost ready.")
health = 3*(int(stats["Constitution"])+random.randint(1,6))
print("Your starting health is",health)
gold=0
print("Rolling for your starting gold. You rolled a ")
rolls=[]
if stats["Charisma"]>=15:
    x=5
else:
    x=0
for n in range(20+x):
    roll=random.randint(1,6)
    rolls.append(roll)
    gold+=roll
for i in rolls:
    print(rolls[i], end = " ")
print("\nYour starting gold is",gold)
    

