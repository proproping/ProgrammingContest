import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b = map(int,input().split())
if a <= b:
    print(a)
else:
    print(a-1)
"""

# B
"""
tmp = list(map(int,input().split()))
K = int(input())
for i in range(K):
    tmp[tmp.index(max(tmp))] = max(tmp)*2
print(sum(tmp))
"""

# C
"""
H,W = map(int,input().split())
s = [list(input()) for _ in range(H)]

def check(h,w):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for k in range(len(dx)):
        if 0 <= h+dy[k] <= (H-1) and 0 <= w+dx[k] <= (W-1):
            if s[h+dy[k]][w+dx[k]] == "#":
                break
            elif k == 3:
                return True
    return False

ans = "Yes"
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            if check(i,j):
                ans = "No"
                break
print(ans)
"""
# D


# E


# F
