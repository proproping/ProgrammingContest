def main():
    N = int(input())
    a = sorted(list(map(int,input().split())),reverse=True)
    ans = 0
    for i in range(1,2*N,2):
        ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()