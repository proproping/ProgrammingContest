import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
ls = sorted(list(map(int,input().split())))
print(sum(ls)-max(ls))
"""
# B
"""
N = int(input())
W = list(map(int,input().split()))
tmp = []
for i in range(N-1):
    tmp.append(abs(sum(W[:i+1])-sum(W[i+1:])))
print(min(tmp))
"""

# C
"""
N,M = map(int,input().split())
a = [int(input()) for _ in range(M)]
booli = [False]*(N+1)
for i in a:
    booli[i] = True
mod = 1000000007
INF = -1
dp = [INF]*(N+1)
dp[0] = 1
if booli[1]:
    dp[1] = 0
else:
    dp[1] = 1
def solve():
    for i in range(2,N+1):
        if booli[i]:
            dp[i] = 0
        else:
            dp[i] = dp[i-1]+dp[i-2]
    return dp[N]%mod
print(solve())
"""

# D
"""
import numpy as np
H,W = map(int,input().split())
mat = [(list(input())) for _ in range(H)]
L = [[0]*W for _ in range(H)]
R = [[0]*W for _ in range(H)]
D = [[0]*W for _ in range(H)]
U = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W-1):
        if mat[i][j] != "#":
            if j == 0:
                L[i][j] = 1
            else:
                L[i][j] = L[i][j-1]+1
        else:
            L[i][j] = 0
for i in range(H):
    for j in range(W-1,-1,-1):
        if mat[i][j] != "#":
            if j == (W-1):
                R[i][j] = 1
            else:
                R[i][j] = R[i][j+1]+1
        else:
            R[i][j] = 0
for i in range(H-1,-1,-1):
    for j in range(W):
        if mat[i][j] != "#":
            if i == (H-1):
                D[i][j] = 1
            else:
                D[i][j] = D[i+1][j]+1
        else:
            D[i][j] = 0
for i in range(H-1):
    for j in range(W):
        if mat[i][j] != "#":
            if i == 0:
                U[i][j] = 1
            else:
                U[i][j] = U[i-1][j]+1
        else:
            U[i][j] = 0
ans = 0
for i in range(H):
    for j in range(W):
        tmp = L[i][j]+R[i][j]+D[i][j]+U[i][j]-3
        if ans < tmp:
            ans = tmp
print(ans)
"""
# E


# F
