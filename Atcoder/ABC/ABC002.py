import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
X,Y = map(int,input().split())
print(max(X,Y))
"""

# B
"""
W = list(input())
for i in range(len(W)):
    if W[i] in ["a","i","u","e","o"]:
        W[i] = ""
print("".join(W))
"""

# C
"""
import numpy as np
tmp = list(map(int,input().split()))
points = [np.array([tmp[i],tmp[i+1]]) for i in range(0,6,2)]
tmp = points[0]
points = [i - tmp for i in points]
print(abs(points[1][0]*points[2][1]-points[1][1]*points[2][0])/2)
"""

# D


# E


# F
