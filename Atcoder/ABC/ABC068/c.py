def main():
    N,M = map(int,input().split())
    ans = "IMPOSSIBLE"
    f = dict(zip(list(range(N)),[0]*N))
    s = dict(zip(list(range(N)),[0]*N))
    for i in range(M):
        a,b = map(lambda x: int(x)-1, input().split())
        if a == 0:
            f[b] = 1
        if b == N-1:
            s[a] = 1
    if len(f) > len(s):
        for i in range(len(s)):
            if s[i] == 1 and f[i] == 1:
                ans = "POSSIBLE"
                break
    else:
        for i in range(len(f)):
            if f[i] == 1 and s[i] == 1:
                ans = "POSSIBLE"
                break
    print(ans)

if __name__ == '__main__':
    main()