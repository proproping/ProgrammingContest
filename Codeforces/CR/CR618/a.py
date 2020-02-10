def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        zero = 0
        for j in range(n):
            if a[j] == 0:
                zero += 1
        if sum(a)+zero == 0:
            zero += 1
        print(zero)


if __name__ == '__main__':
    main()