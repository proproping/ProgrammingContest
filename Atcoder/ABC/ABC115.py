import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
D = int(input())
ans = "Christmas"
for i in range(25-D):
    ans += " Eve"
print(ans)
"""

# B
"""
p = []
N = int(input())
for i in range(N):
    p.append(int(input()))
ans = sum(p)-(max(p)/2)
print(int(ans))
"""

# C
"""
N,K = map(int,input().split())
h = sorted([int(input()) for i in range(N)])
tmp = []
for i in range(N-K+1):
    tmp.append(h[i+K-1]-h[i])
print(min(tmp))
"""

# D


# E


# F
