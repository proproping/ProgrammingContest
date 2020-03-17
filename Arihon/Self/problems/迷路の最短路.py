from collections import deque
INF = 10**9

def bfs(s):
    global cost
    q = deque([s])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while len(q) != 0:
        tmp = q.popleft()
        i,j = tmp[0],tmp[1]
        if maze[i][j] == "G":
            break
        for k in range(4):
            ni,nj = i-dy[k],j-dx[k]
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] != "#" and cost[ni][nj] == INF:
                    q.append([ni,nj])
                    cost[ni][nj] = cost[i][j] + 1
    return cost[i][j]


def main():
    global N,M,maze,cost
    N,M = map(int,input().split())
    maze = [list(input()) for _ in range(N)]
    cost = [[INF]*M for _ in range(N)]
    s = 0
    flag = False
    for i in range(N):
        if flag:
            break
        for j in range(M):
            if maze[i][j] == "S":
                cost[i][j] = 0
                s = [i,j]
                flag = True
    print(bfs(s))

if __name__ == '__main__':
    main()

"""
in

10 10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#

out
22
"""