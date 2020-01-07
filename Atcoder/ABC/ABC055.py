import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
x = 800*N
y = 200*(N//15)
print(x-y)
"""

# B
"""
from math import factorial
N = int(input())
print(factorial(N)%(10**9+7))
"""

# C
"""
N,M = map(int,input().split())
count = 0
if N <= M//2:
    count += N
    M -= N*2
else:
    count += M//2
    M = 0
count += M//4
print(count)
"""
# D


# E


# F
