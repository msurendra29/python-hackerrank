#!/bin/python3

import sys

c1 = 0
sum1 = 0
sum2 = 0
n = int(input().strip())
c2 = n-1
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in a:
    sum1 = sum1 + a[c1][c1]
    c1 = c1 + 1
    
for i in a:
    sum2 = sum2 + a[c2][c2]
    c2 = c2 - 1
print(abs(sum1,sum2))
