def main():
    N = int(input())
    d = sorted(list(map(int,input().split())))
    low = d[N//2-1]
    high = d[N//2]
    print(high-low)

if __name__ == '__main__':
    main()