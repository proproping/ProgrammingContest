def main():
    N,W = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j-wv[i][0] >= 0:
                dp[i+1][j] = max(dp[i][j],dp[i][j-wv[i][0]]+wv[i][1])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])

if __name__ == '__main__':
    main()