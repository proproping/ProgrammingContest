def main():
    import math
    N = int(input())
    ab = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += ab[i][0] * ab[i][1]
    print(math.floor(ans*1.05))

if __name__ == '__main__':
    main()