import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A = int(input())
B = int(input())
C = int(input())
ans = [0]*3
tmp1 = [A,B,C]
tmp2 = sorted([A,B,C],reverse = 1)
for i in range(3):
    for j in range(3):
        if tmp1[i] == tmp2[j]:
            ans[i] += j+1
for i in range(3):
    print(ans[i])
"""

# B
"""
S = input()
N = int(input())
lr = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    atmp = S[:lr[i][0]-1]
    btmp = list(S[lr[i][0]-1:lr[i][1]])
    btmp.reverse()
    btmp = "".join(btmp)
    ctmp = S[lr[i][1]:]
    S = atmp+btmp+ctmp
print(S)
"""

# C


# D


# E


# F
