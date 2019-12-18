import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C,D = map(int,input().split())
print(max([A*B,C*D]))
"""

# B
"""
N = int(input())
S = input()
tmp = 0
ans = 0
for i in range(N):
    if S[i] == "I":
        tmp += 1
    else:
        tmp += -1
    ans = max([ans,tmp])
print(ans)
"""

# C


# D


# E


# F
