def main():
    N = int(input())
    p = list(map(int,input().split()))
    ans = 0
    i = 0
    while True:
        if i >= N:
            break
        if i+1 == p[i]:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)

if __name__ == '__main__':
    main()