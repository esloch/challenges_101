#Poker Dice Challenge - www.101computing.net/fancy-a-game-of-poker-dice/
import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)

print("Die 1: " + str(die1))
print("Die 2: " + str(die2))
print("Die 3: " + str(die3))


if die1 ==die2 and die2 == die3:
    print("Three of a kind!")

elif die1 == die2 or die2==die3 or die1 == die3:
    print("Two pair!")

elif die1 != die2 and die2 != die3 and die1 != die3:
    print("Better luck next time!!")
    


print(80 * "-")    
    
dices_list = []


dices_list.append(die1)
dices_list.append(die2)
dices_list.append(die3)

print(dices_list, "=",sum(dices_list))


# TODO: need to check each digit
if sum(dices_list) % 2 == 0:
    print(f"The 3 dice are all even numbers {dices_list}")
else:
    print(f"The 3 dice are all odd numbers {dices_list}.")
