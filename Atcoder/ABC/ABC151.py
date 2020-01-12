import sys
import os
f = open('input.txt','r')
sys.stdin = f

#A
"""
C = input()
ls = list("abcdefghijklmnopqrstuvwxyz")
num = list(range(0,26))
dic = dict(zip(ls,num))
print(ls[dic[C]+1])
"""
#B
"""
N,K,M = map(int,input().split())
A = list(map(int,input().split()))
tmp1 = sum(A)
tmp2 = N*M
if tmp2 - tmp1 <= K:
    print(max(0,tmp2-tmp1))
else:
    print(-1)
"""

#C
"""
N,M = map(int,input().split())
dic = dict(zip(list(range(1,N+1)),[0]*N))
bl = [True]*N
ac,wa = 0,0
for i in range(M):
    p,s = input().split()
    if s == "WA":
        dic[int(p)] += 1
    elif s == "AC":
        if bl[int(p)-1]:
            ac += 1
            wa += dic[int(p)]
            bl[int(p)-1] = False
print(ac,wa)
"""

#D
"""
from collections import deque
H,W = map(int,input().split())
maze = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(H):
    maze.append(list(input()))
def bfs(sx,sy):
    INF = -1
    cost = [[INF]*W for _ in range(H)]
    P = deque()
    P.append([sx,sy])
    cost[sx][sy] = 0
    while len(P) != 0:
        p = P.popleft()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != "#" and cost[nx][ny] == INF:
                P.append([nx,ny])
                cost[nx][ny] = cost[p[0]][p[1]]+1
    return cost
def solve():
    ans = 0
    for i in range(H):
        for j in range(W):
            if maze[i][j] != "#":
                sx,sy = i,j
                cs = bfs(sx,sy)
                for k in range(len(cs)):
                    if max(cs[k]) > ans:
                        ans = max(cs[k])
    return ans
print(solve())
"""

#E

#F