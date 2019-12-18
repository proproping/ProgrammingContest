import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
X,Y = map(int,input().split())
ans = 0
if X == 3:
    ans += 100000
if X == 2:
    ans += 200000
if X == 1:
    ans += 300000
if Y == 3:
    ans += 100000
if Y == 2:
    ans += 200000
if Y == 1:
    ans += 300000
if X == 1 and Y == 1:
    ans += 400000
print(ans)
"""

# B
"""
import numpy
N = int(input())
A = list(map(int,input().split()))
tmp1 = [A[0]]
tmp2 = [sum(A)]
for i in range(1,N):
    tmp1.append(tmp1[i-1]+A[i])
    tmp2.append(tmp2[i-1]-A[i-1])
tmp1 = numpy.array(tmp1)
tmp2 = numpy.array(tmp2)
ans = list(map(abs,list(tmp1 - tmp2)))
print(min(ans))
"""

# C


# D


# E


# F
