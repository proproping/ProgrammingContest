def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 10**9
    for i in range(1,101):
        tmp = sum([(X[j]-i)**2 for j in range(N)])
        ans = min(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()