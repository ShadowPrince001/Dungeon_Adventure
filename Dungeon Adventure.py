import random
hp1 =20
hp2 =2
choices = ["up high", "in the middle" ,"down low"]
print("Welcome to the dungeon!There is a hobgoblin here.")
while hp1 > 0 and hp2 > 0:
    atk1 = random.choice(choices)

    dfens1 = input(" It is attacking you. You may defend up high, in the middle or down low. Choose where u want to defend: ")
    if dfens1 not in choices:
        print("Sorry i didn't understand you. The Hobgoblin is attacking you.")
    elif atk1!= dfens1:
        dmg1 = random.randint(7,10)
        hp1 = hp1 - dmg1
        if hp1 <= 0:
            hp1 =0
        print(f"The hobgoblin attacked you {atk1}.  You defended {dfens1}. The hobgoblin hit you and did {dmg1} damage. You now have {hp1} health remaining")
        if hp1 == 0:   
            print("Oh no! The hobogblin has killed you. The hobgoblin searched your dead body and took all yours belonging")   
            break  
    else:
         print(f"The hobgoblin attacked you {atk1}.  You defended {dfens1}. You defended the hobgoblin's attack")        
    dfens2 = random.choice(choices)
    atk2 = input("It is your turn. You are attacking the hobgoblin. You may attack up high, in the middle or down low. Choose where u want to attack: ")

    if atk2 not in choices:
        print("Sorry i didn't understand you. You are attacking the hobgoblin. You may attack up high, in the middle or down low. Choose where u want to attack: ")
    elif atk2!= dfens2:
        dmg2 = random.randint(7,10)
        hp2 = hp2 - dmg2
        if hp2 <= 0:
            hp2 =0
        print(f"You attacked the hobgoblin {atk2}.  The hobgoblin defended {dfens2}. You hit the hobgoblin and did {dmg2} damage. The hobogblin now has {hp2} health remaining")
        if hp2 == 0:
            print("Bazinga! You have killed the hobgoblin. You searched it dead body and got 50 golden coins")
    else:
        print(f"You attacked the hobgoblin {atk2}.  The hobgoblin defended {dfens2}. The hobgoblin defended your attack")
