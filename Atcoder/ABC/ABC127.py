import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
ans = B
if A >= 13:
    print(ans)
elif 6 <= A <= 12:
    print(int(ans/2))
else:
    print(0)
"""

# B
"""
r,D,x2000 = map(int,input().split())
xi = r*x2000-D
for i in range(10):
    print(xi)
    xi = r*xi-D
"""

# C
"""
N,M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(M)]
L = 0
R = 10**5+1
for i in range(M):
    if L < mat[i][0]:
        L = mat[i][0]
    if R > mat[i][1]:
        R = mat[i][1]
print(max([R-L+1,0]))
"""

# D


# E


# F
