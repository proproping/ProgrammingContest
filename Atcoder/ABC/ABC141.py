import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a = str(input())
if a == "Sunny":
    print("Cloudy")
elif a == "Cloudy":
    print("Rainy")
else:
    print("Sunny")
"""

# B
"""
a = list(str(input()))
odd = a[0::2]
even = a[1::2]
if ("L" not in odd) and ("R" not in even):
    print("Yes")
else:
    print("No")
"""

# C
"""
import numpy as np
N,K,Q = map(int,input().split())
A = [int(input()) for x in range(Q)]
points = [K]*N
tmp = [1]*N
for i in range(Q):
    points[A[i]-1] += 1
points = list(np.array(points) - Q)
for i in range(len(points)):
    if points[i] > 0:
        print("Yes")
    else:
        print("No")
"""

# D


# E


# F
