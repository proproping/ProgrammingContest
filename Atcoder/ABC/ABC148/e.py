def main():
    N = int(input())
    if N%2 == 1:
        print(0)
    else:
        ans = 0
        N //= 2
        while N > 0:
            ans += N // 5
            N //= 5
        print(ans)

if __name__ == '__main__':
    main()