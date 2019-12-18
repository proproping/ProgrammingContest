import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
tmp = 0
count = 0
while tmp < B:
    tmp += A
    count += 1
print(count)
"""

# B
"""
import numpy as np
N = int(input())
mat = [list(input()) for i in range(N)]
mat = np.array(mat)
ans = np.rot90(mat,k = -1)
for i in range(N):
    print("".join(ans[i]))
"""

# C


# D


# E


# F
