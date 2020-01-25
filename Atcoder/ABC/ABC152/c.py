def main():
    N = int(input())
    P = list(map(int,input().split()))
    ans = 0
    minx = 10**9
    for i in range(N):
        if minx > P[i]:
            ans += 1
            minx = P[i]
    print(ans)

if __name__ == '__main__':
    main()