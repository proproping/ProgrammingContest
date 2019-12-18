import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = list(map(str,input().split(",")))
tmp = " ".join(S)
print(tmp)
"""

# B
"""
K,S = map(int,input().split())
count = 0
for i in range(K+1):
    for j in range(K+1):
        X = i
        Y = j
        Z = S - i - j
        if 0 <= Z <= K:
            count += 1
print(count)
"""

# C


# D


# E


# F
