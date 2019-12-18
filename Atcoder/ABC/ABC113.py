import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
X,Y = map(int,input().split())
print(int(X+(Y/2)))
"""

# B
"""
N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
tmp = []
for i in range(N):
    H[i] = abs((T-H[i]*0.006)-A)
ans = min(H)
for j in range(N):
    if H[j] == ans:
        ans = j+1
print(ans)
"""

# C


# D


# E


# F
