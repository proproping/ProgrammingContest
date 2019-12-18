import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b,c,d = map(int,input().split())
if abs(a-c) <= d or (abs(a-b) <= d and abs(b-c) <= d):
    print("Yes")
else:
    print("No")
"""

# B
"""
from math import floor
X = int(input())
if X != 1000:
    tmp = []
    for i in range(2,100):
        tmp.append(floor(X**(1/i))**i)
    print(max(tmp))
else:
    print(1000)
"""

# C


# D


# E


# F
