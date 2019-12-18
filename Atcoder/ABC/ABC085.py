import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()
tmp = list(S)
tmp[3] = "8"
print("".join(tmp))
"""

# B
"""
N = int(input())
d = set([int(input()) for i in range(N)])
print(len(d))
"""

# C
"""
N,Y = map(int,input().split())
x = 0
y = 0
z = 0
for i in range(N):
    if (Y-10000*x)/5000 == (N-x):
        break
    else:
        x += 1
for j in range(N):
    if (Y-10000*x-5000*y)/1000 == (N-x-y):
        break
    else:
        y += 1
for k in range(N):
    if (Y-10000*x-5000*y-1000*z) == 0:
        break
    else:
        z += 1
ans = [x,y,z]
if (Y-10000*x-5000*y-1000*z) == 0:
    print(*ans,sep=" ")
else:
    print("-1 -1 -1")
"""

# D


# E


# F
