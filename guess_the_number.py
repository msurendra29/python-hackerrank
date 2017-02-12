import sys
import os
import random
import time
import calendar

# script


def compare_guess_with_dice(g):
    if(int(g) == int(dice_roll)):
        print("Your guess is correct",g)
    elif ((int(g)+1 == int(dice_roll)) or (int(g)-1 == int(dice_roll))):
        print("Your guess is just miss ", g,dice_roll)
    else:
        print("Your guess is wrong",g,dice_roll)
    
Flag = False
while Flag == False:
    dice_roll = random.randint(1,6)
    print("dice: ",dice_roll)
    print("Guess the number on the Dice")
    guess = input()
    compare_guess_with_dice(guess)
    print("Do you want to roll Again? ")
    print("Press Y for Yes and N for No")
    res = input()
    if res == 'Y':
        Flag = False
    elif res == 'N':
        Flag = True
    else:
        print("Please enter Yes or No")

#script ending
