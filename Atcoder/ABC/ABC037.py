import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C = map(int,input().split())
ans = 0
ans += (C//min([A,B]))
ans += ((C-ans*min([A,B]))//max([A,B]))
print(ans)
"""

# B
"""
N,Q = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(Q)]
ans = [0]*N
for i in range(Q):
    for j in range(mat[i][0]-1,mat[i][1]):
        ans[j] = mat[i][2]
for k in range(len(ans)):
    print(ans[k])
"""

# C


# D


# E


# F
