def main():
    from operator import itemgetter
    N,D,A = map(int,input().split())
    XH = sorted([list(map(int,input().split())) for _ in range(N)],key=itemgetter(0))
    i = 0
    ans = 0
    bom = []
    while i < N:
        s = XH[i][0]
        while i < N and XH[i][0] <= s + D:
            i += 1
        p = XH[i-1][0]
        while i < N and XH[i][0] <= p + D:
            i += 1
        print(i)
        ans += 1


if __name__ == '__main__':
    main()