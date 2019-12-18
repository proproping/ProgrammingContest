import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A = int(input())
print((A/2)**2)
"""

# B
"""
from math import pi
N = int(input())
R = sorted([int(input()) for i in range(N)])
flag = 1
r = 0
for i in range(N):
    if flag == 1:
        r += R[-i-1]**2
        flag = 0
    else:
        r += -R[-i-1]**2
        flag = 1
print(r*pi)
"""

# C


# D


# E


# F
