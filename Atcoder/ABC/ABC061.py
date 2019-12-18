import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C = map(int,input().split())
if A <= C <= B:
    print("Yes")
else:
    print("No")
"""

# B
"""
import collections
N,M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(M)]
tmp = []
for i in range(M):
    tmp = tmp + mat[i]
ans = collections.Counter(tmp)
for j in range(N):
    print(ans[j+1])
"""

# C


# D


# E


# F
