def main():
    N,A,B = map(int,input().split())
    ans = (N//(A+B))*A
    ans += min(A,N%(A+B))
    print(ans)

if __name__ == '__main__':
    main()