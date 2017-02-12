import sys
import math
S = 1
P = 0
t = int(input())
for i in range(t):
    n = int(input())
    H = [int(health) for health in input().split(' ')]
    H = H[:n]
    H.sort()
    flag = True
    eat_no_mandragoras  = 0
    new_P = 0    
    for i in range(n):
        total_hp = sum(map(int,H[eat_no_mandragoras:]))               
        new_P = S * total_hp
        if(new_P > P):
            P = new_P
            S = S + 1
            eat_no_mandragoras = eat_no_mandragoras + 1
        else:
            break
    print(P)
