import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
c1 = input()
c2 = input()
c3 = input()
print("".join([c1[0],c2[1],c3[2]]))
"""

# B
"""
A,B = map(int,input().split())
tmp = []
count = 0
for i in range(A,B+1):
    tmp.append(i)
for j in range(len(tmp)):
    flag = 1
    if len(str(tmp[j]))%2 == 0:
        for k in range(int(len(str(tmp[j]))/2)):
            if str(tmp[j])[k] != str(tmp[j])[-k-1]:
                flag = 0
                break
    else:
        for l in range(int(len(str(tmp[j]))//2)):
            if str(tmp[j])[l] != str(tmp[j])[-l-1]:
                flag = 0
                break
    if flag == 1:
        count += 1
print(count)
"""

# C
"""
N,M = map(int,input().split())
"""
"""
mat = [[0]*M for _ in range(N)]
dx = [-1,0,1,-1,0,1,-1,0,1]
dy = [1,1,1,0,0,0,-1,-1,-1]
for i in range(N):
    for j in range(M):
        for k in range(9):
            if 0 <= i+dy[k] <= (N-1) and 0 <= j+dx[k] <= (M-1):
                mat[i+dy[k]][j+dx[k]] += 1
print(mat)
"""
"""
if N == 1 or M == 1:
    if N == M:
        print(1)
    else:
        print(N*M-2)
else:
    print(N*M-2*(N+M-2))
"""
# D


# E


# F
