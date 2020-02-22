def main():
    INF = float('inf')
    N,M = map(int,input().split())
    s,c = [],[]
    for i in range(M):
        t1,t2 = input().split()
        t1 = t1.replace('Y','1').replace('N','0')
        s.append(int(t1,2))
        c.append(int(t2))
    dp = [[INF]*(2**N) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(2**N):
            dp[i+1][j|s[i]] = min(dp[i+1][j|s[i]],dp[i][j] + c[i])
            dp[i+1][j] = min(dp[i+1][j],dp[i][j])
    if dp[M][2**N-1] == INF:
        print(-1)
    else:
        print(dp[M][2**N-1])

if __name__ == '__main__':
    main()