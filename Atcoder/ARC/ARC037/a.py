def main():
    N = int(input())
    m = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += max(0,80-m[i])
    print(ans)

if __name__ == '__main__':
    main()