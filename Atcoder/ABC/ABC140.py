import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
print(N**3)
"""

# B
"""
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
u = sum(b)
for i in range(1,n):
    if a[i] - a[i-1] == 1:
        u = u + c[a[i]-2]
print(u)
"""

# C
"""
N = int(input())
B = list(map(int,input().split()))
A = [0]*N
A[0] = B[0]
for i in range(1,N-1):
    if B[i-1] < B[i]:
        A[i] = B[i-1]
    else:
        A[i] = B[i]
A[-1] = B[-1]
print(sum(A))
"""

# D


# E


# F
