m, n, mat, ans = 0, 0, 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def main():
    global m, n, mat, tmp,ans
    m, n = [int(input()) for _ in range(2)]
    mat = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                dfs(i, j, mat, 0)
    print(ans)

def dfs(i, j, mat, c):
    global dx,dy,ans
    mat[i][j] = 0
    c += 1
    for k in range(4):
        if (0 <= i + dy[k] <= n - 1) and (0 <= j + dx[k] <= m - 1):
            if mat[i + dy[k]][j + dx[k]] == 1:
                dfs(i + dy[k], j + dx[k], mat, c)
    mat[i][j] = 1
    ans = max(ans,c)

if __name__ == '__main__':
    main()