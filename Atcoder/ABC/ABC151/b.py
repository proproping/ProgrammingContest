def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    tmp1 = sum(A)
    tmp2 = N*M
    if tmp2 - tmp1 <= K:
        print(max(0,tmp2-tmp1))
    else:
        print(-1)

if __name__ == '__main__':
    main()