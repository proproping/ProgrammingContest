import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C = map(int,input().split())
if A <= C <= B:
    print("Yes")
else:
    print("No")
"""

# B
"""
import collections
N,M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(M)]
tmp = []
for i in range(M):
    tmp = tmp + mat[i]
ans = collections.Counter(tmp)
for j in range(N):
    print(ans[j+1])
"""

# C
"""
from operator import itemgetter
N,K = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(N)]
ls = sorted(ls,key=itemgetter(0))
len = 0
ans = 0
i = 0
while True:
    if len >= K:
        break
    ans = ls[i][0]
    len += ls[i][1]
    i += 1
print(ans)
"""

# D


# E


# F
