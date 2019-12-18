import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
if B%A == 0:
    print(A+B)
else:
    print(B-A)
"""

# B
"""
N,M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
K = []
for i in range(N):
    K.append(A[i].pop(0))
ans = A[0]
for j in range(1,N):
    ans = set(ans)&set(A[j])
print(len(ans))
"""

# C
"""
import math
N = int(input())
A = list(map(int,input().split()))
gcd = 10**9
for i in range(N-1):
    tmp = math.gcd(A[i],A[i+1])
    if tmp < gcd:
        gcd = tmp
print(gcd)
"""

# D


# E


# F
