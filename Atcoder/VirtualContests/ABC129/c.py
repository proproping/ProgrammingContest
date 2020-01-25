def main():
    N,M = map(int,input().split())
    a = [int(input()) for _ in range(M)]
    booli = [False]*(N+1)
    for i in a:
        booli[i] = True
    mod = 1000000007
    INF = -1
    dp = [INF]*(N+1)
    dp[0] = 1
    if booli[1]:
        dp[1] = 0
    else:
        dp[1] = 1
    def solve():
        for i in range(2,N+1):
            if booli[i]:
                dp[i] = 0
            else:
                dp[i] = dp[i-1]+dp[i-2]
        return dp[N]%mod
    print(solve())

if __name__ == '__main__':
    main()