def main():
    import math
    from operator import itemgetter
    N,D,A = map(int,input().split())
    XH = [sorted([list(map(int,input().split())) for _ in range(N)],key=itemgetter(0))]
    i,ans = 0,0
    j = 0
    while i < N:
        s = XH[i][0]
        i += 1
        while (i < N) and (XH[i][0] <= s + D):
            i += 1
        p = XH[i-1][0]
        while (i < N) and (XH[i][0] <= p + D):
            i += 1
        ans += math.ceil(max([k[1] for k in XH[j:i]])/A)
        j = i
    print(ans)

if __name__ == '__main__':
    main()