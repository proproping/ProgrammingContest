def main():
    INF = 10**9
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    dp = [INF]*N
    dp[0] = 0
    for i in range(N):
        for j in range(1,K+1):
            if i-j >= 0:
                dp[i] = min(dp[i],abs(h[i]-h[i-j])+dp[i-j])
    print(dp[N-1])

if __name__ == '__main__':
    main()