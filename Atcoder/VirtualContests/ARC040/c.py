def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    M = len(S[0])
    ans = 0
    for i in range(N-1,-1,-1):
        for j in range(M):
            if S[i][j] == ".":
                for k in range(j,M):
                    S[i][k] = "o"
                for k in range(j+1):
                    S[max(0,i-1)][k] = "o"
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()