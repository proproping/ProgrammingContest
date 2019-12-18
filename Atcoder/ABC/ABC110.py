import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C = map(int,input().split())
print(max(A,B,C)*10+A+B+C-max(A,B,C))
"""

# B
"""
N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
ans = "War"
for i in range(X+1,Y):
    if max(x) < i and min(y) >= i:
        ans = "No War"
        break
print(ans)
"""

# C


# D


# E


# F
