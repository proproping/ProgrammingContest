from collections import deque

def dfs(x,y):
    global field,N,M
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [1,1,1,0,0,-1,-1,-1]
    q = deque([[x,y]])
    while len(q) != 0:
        tmp = q.pop()
        i,j = tmp[0],tmp[1]
        field[i][j] = "."
        for k in range(8):
            if 0 <= i-dy[k] < N and 0 <= j-dx[k] < M:
                if field[i-dy[k]][j-dx[k]] == "W":
                    q.append([i-dy[k],j-dx[k]])

def main():
    global field,N,M
    N,M = map(int,input().split())
    field = [list(input()) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == "W":
                dfs(i,j)
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()

"""
in
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.

out
3
"""