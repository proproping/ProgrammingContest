import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,op,B = input().split()
if op == "+":
    print(int(A)+int(B))
else:
    print(int(A)-int(B))
"""

# B
"""
N = int(input())
T = list(map(int,input().split()))
M = int(input())
mat = [list(map(int,input().split())) for i in range(M)]
ans = [0]*M
time = sum(T)
for i in range(M):
    ans[i] = time-T[mat[i][0]-1]+mat[i][1]
for j in range(len(ans)):
    print(ans[j])
"""

# C


# D


# E


# F
