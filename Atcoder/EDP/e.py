def main():
    INF = float('inf')
    N,W = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(N)]
    sumv = sum([v for w,v in wv])
    dp = [[INF]*(sumv+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(sumv+1):
            if j-wv[i][1] >= 0:
                dp[i+1][j] = min(dp[i][j],dp[i][j-wv[i][1]]+wv[i][0])
            else:
                dp[i+1][j] = dp[i][j]
    ans = 0
    for i in range(sumv+1):
        if dp[N][i] <= W:
            ans = max(ans,i)
    print(ans)
if __name__ == '__main__':
    main()