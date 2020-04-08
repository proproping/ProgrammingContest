def main():
    N = int(input())
    dp = [0] * (N+1)
    for i in range(N+1):
        dp[i] += 1
        next = i + sum(map(int, list(str(i))))
        if next < (N+1):
            dp[next] += dp[i]
    print(dp[N])

if __name__ == '__main__':
    main()