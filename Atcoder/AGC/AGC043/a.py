INF = float('inf')

def main():
    H,W = map(int,input().split())
    mat = [list(input()) for _ in range(H)]
    dp = [[INF] * W for _ in range(H)]
    if mat[0][0] == "#":
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1]
                if mat[i][j] == "#":
                    dp[i][j] += 1
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
                if mat[i][j] == "#":
                    dp[i][j] += 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
                if mat[i][j] == "#":
                    dp[i][j] += 1
    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()