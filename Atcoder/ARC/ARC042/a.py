def main():
    N,M = map(int,input().split())
    a = [int(input()) for _ in range(M)]
    bot = sorted(list(set(range(1,N+1)) - set(a)))
    tf = [False]*N
    ans = []
    for i in range(M-1,-1,-1):
        if tf[a[i]-1] == False:
            tf[a[i]-1] = True
            ans.append(a[i])
    for i in range(len(ans)):
        print(ans[i])
    for i in range(len(bot)):
        print(bot[i])


if __name__ == '__main__':
    main()