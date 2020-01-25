def main():
    N = int(input())
    ans = 0
    for i in range(N):
        ans += (i+1)/N*10000
    print(int(ans))

if __name__ == '__main__':
    main()