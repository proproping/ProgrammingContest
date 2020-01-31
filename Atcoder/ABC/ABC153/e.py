def main():
    H,N = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    maxA = max(A for A,B in AB)
    dp = [0]*(H+maxA)
    for i in range(1,H+maxA):
        dp[i] = min(dp[i-A]+B for A,B in AB)
    print(min(dp[H:]))


if __name__ == '__main__':
    main()
