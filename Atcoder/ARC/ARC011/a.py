def main():
    m,n,N = map(int,input().split())
    ans = N
    new = N
    rec = 0
    while new > 0:
        rec += new
        new = rec//m*n
        rec = rec%m
        ans += new

    print(ans)

if __name__ == '__main__':
    main()