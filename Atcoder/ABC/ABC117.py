import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
T,X = map(int,input().split())
print(T*1/X)
"""

# B
"""
N = int(input())
L = list(map(int,input().split()))
if max(L) < (sum(L)-max(L)):
    print("Yes")
else:
    print("No")
"""

# C
"""
N,M = map(int,input().split())
X = sorted(list(map(int,input().split())))
if N >= M:
    print(0)
else:
    gap = []
    for i in range(M-1):
        gap.append(abs(X[i+1]-X[i]))
    gap = sorted(gap,reverse = 1)
    print(sum(gap[N-1:]))
"""

# D


# E


# F
