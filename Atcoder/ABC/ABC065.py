import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
X,A,B = map(int,input().split())
if X < abs(A-B):
    print("dangerous")
elif A-B >= 0:
    print("delicious")
else:
    print("safe")
"""

# B
"""
N = int(input())
a = [int(input()) for i in range(N)]
count = 0
tmp = 1
flag = 0
for i in range(len(a)):
    if tmp == 2:
        flag = 1
        break
    else:
        tmp = a[tmp-1]
    count += 1
if flag == 1:
    print(count)
else:
    print(-1)
"""

# C
"""
import math
mod = 10**9+7
N,M = map(int,input().split())
if abs(N-M) > 1:
    print(0)
elif N == M:
    print((math.factorial(N)*math.factorial(M)*2)%mod)
else:
    print((math.factorial(N)*math.factorial(M))%mod)
"""

# D


# E


# F
