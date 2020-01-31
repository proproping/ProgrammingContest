def main():
    N = int(input())
    p = list(map(float,input().split()))
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(i+1):
            dp[i+1][j] += dp[i][j] * (1-p[i])
            dp[i+1][j+1] += dp[i][j] * p[i]
    print(sum(dp[N][N//2+1:]))


if __name__ == '__main__':
    main()