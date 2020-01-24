import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from collections import deque
    H,W = map(int,input().split())
    maze = []
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    ls = []
    count = 0
    for i in range(H):
        tmp = list(input())
        maze.append(tmp)
        for j in range(W):
            if tmp[j] != "#":
                ls.append([i,j])
                count += 1
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
        for i in ls:
            sx,sy = i[0],i[1]
            cs = bfs(sx,sy)
            for k in range(len(cs)):
                if ans == count:
                    break
                if max(cs[k]) > ans:
                    ans = max(cs[k])
        return ans
    print(solve())

if __name__ == '__main__':
    main()