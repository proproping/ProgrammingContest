import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
x,a,b = map(int,input().split())
if abs(x-a) > abs(x-b):
    print("B")
else:
    print("A")
"""

# B
"""
S = input()
tmp = list("abcdefghijklmnopqrstuvwxyz")
ans = []
for i in range(len(tmp)):
    if tmp[i] not in S:
        ans.append(tmp[i])
if len(ans) == 0:
    print("None")
else:
    print(ans[0])
"""

# C


# D


# E


# F
