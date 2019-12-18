import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
H,W = map(int,input().split())
h,w = map(int,input().split())
print(H*W-h*W-(w*(H-h)))
"""

# B
"""
import numpy as np
N,M,C = map(int,input().split())
B = np.array(list(map(int,input().split())))
A = []
for i in range(N):
    A.append(np.array(list(map(int,input().split()))))
count = 0
for i in range(N):
    if sum(list(A[i]*B))+C > 0:
        count += 1
print(count)
"""

# C
"""
from operator import itemgetter
N,M = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(N)]
ls = sorted(ls,key=itemgetter(0))
ans = 0
pon = 0
for i in range(N):
    if pon < M:
        pon += ls[i][1]
        ans += ls[i][1]*ls[i][0]
    else:
        i = i-1
        break
if pon == M:
    print(ans)
else:
    ans -= ls[i][0]*(pon - M)
    print(ans)
""" 
# D


# E


# F
