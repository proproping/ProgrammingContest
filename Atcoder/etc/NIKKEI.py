import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
from math import ceil
N = int(input())
print(ceil(N/2)-1)
"""

# B
"""
N = int(input())
D = list(map(int,input().split()))
"""

# C
"""
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
ans = "YES"
for i in range(N):
    if A[i] > B[i]:
        ans = "NO"
        break
print(ans)
"""

# D
"""
N,M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(M)]
"""

# E


# F
