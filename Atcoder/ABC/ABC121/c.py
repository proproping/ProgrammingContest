def main():
    from operator import itemgetter
    N,M = map(int,input().split())
    ls = [list(map(int,input().split())) for _ in range(N)]
    ls = sorted(ls,key=itemgetter(0))
    ans = 0
    pon = 0
    for i in range(N):
        if pon < M:
            pon += ls[i][1]
            ans += ls[i][1]*ls[i][0]
        else:
            i = i-1
            break
    if pon == M:
        print(ans)
    else:
        ans -= ls[i][0]*(pon - M)
        print(ans)

if __name__ == '__main__':
    main()