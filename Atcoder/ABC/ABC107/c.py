def main():
    INF = 10**18
    N,K = map(int,input().split())
    x = list(map(int,input().split()))
    ans = INF
    for i in range(K-1,N):
        ans = min(ans,abs(x[i]-x[i-K+1])+min(abs(0-x[i]),abs(0-x[i-K+1])))
    print(ans)

if __name__ == '__main__':
    main()