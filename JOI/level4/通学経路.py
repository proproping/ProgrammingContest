def main():
    a, b = map(int, input().split())
    dp = [[0] * a for _ in range(b)]
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        dp[y - 1][x - 1] = -1
    dp[0][0] = 1
    for i in range(a):
        for j in range(b):
            if dp[j][i] == -1:
                continue
            if 0 <= (j-1) and dp[j - 1][i] != -1:
                dp[j][i] += dp[j - 1][i]
            if 0 <= (i-1) and dp[j][i - 1] != -1:
                dp[j][i] += dp[j][i - 1]
    print(dp[b - 1][a - 1])

if __name__ == '__main__':
    main()