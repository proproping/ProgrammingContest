import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
if A%3 == 0 or B%3 == 0 or (A+B)%3 == 0:
    print("Possible")
else:
    print("Impossible")
"""

# B
"""
N,K = map(int,input().split())
l = sorted(list(map(int,input().split())),reverse = 1)
print(sum(l[:K]))
"""

# C
"""
import numpy as np
N = int(input())
a = list(map(int,input().split()))
x = np.array([0]*(N))
suma = sum(a)
for i in range(1,N):
    x[i] = x[i-1] + a[i-1]
y = np.array([suma]*(N))-x
ans = list(map(abs,x-y))
print(min(ans[1:]))
"""

# D


# E


# F
