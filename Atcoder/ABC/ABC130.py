import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
x,a = map(int,input().split())
if x < a:
    print(0)
else:
    print(10)
"""

# B
"""
N,X = map(int,input().split())
L = list(map(int,input().split()))
D = 0
count = 1
for i in range(N):
    D = D + L[i]
    if D <= X:
        count += 1
print(count)
"""

# C
"""
W,H,x,y = map(float,input().split())
if y == (H/W)*x and y == H - (H/W)*x:
    tf = 1
else:
    tf = 0
print(" ".join([str(W*H/2),str(tf)]))
"""

# D


# E


# F
