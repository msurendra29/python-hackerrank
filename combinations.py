#!/bin/python3

import sys
import itertools


#n = int(input().strip())
#number = input().strip()
# your code goes here
magic = lambda nu: ("".join(str(i) for i in nu))
stuff = [9, 6, 8]
for L in range(0,len(stuff)+1):
    for subset in itertools.combinations(stuff,L):
        sublist = list(subset)
        print((magic(sublist)))
        

