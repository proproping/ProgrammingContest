import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
n,x = map(int,input().split())
print(x-1) if (x-1) < (n-x) else print(n-x)
"""

# B
"""
n = int(input())
h = 1
w = 1
tmp = []
while h*w <= n:
    w = n//h
    tmp.append(abs(h-w)+n-h*w)
    h += 1
    w = 1
print(min(tmp))
"""

# C


# D


# E


# F
