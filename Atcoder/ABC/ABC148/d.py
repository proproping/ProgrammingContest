def main():
    N = int(input())
    a = list(map(int,input().split()))
    check = 1
    count = 0
    if 1 not in a:
        print(-1)
    else:
        for i in range(N):
            if a[i] != check:
                count += 1
            else:
                check += 1
        print(count)

if __name__ == '__main__':
    main()