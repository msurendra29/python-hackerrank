import sys
import os
import random
import time
import calendar

# script
Flag = False
while Flag == False:
    print(random.randint(1,6))
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
