def main():
    N,K = map(int,input().split())
    t = [int(input()) for _ in range(N)]
    ans = -1
    for i in range(2,N):
        tmp = t[i-2:i+1]
        if sum(tmp) < K:
            ans = i+1
            break
    print(ans)

if __name__ == '__main__':
    main()