def main():
    N = int(input())
    ans = 0
    for i in range(N):
        tmp = list(map(int,input().split()))
        point = sum(tmp[:4])+tmp[4]*110/900
        ans = max(ans,point)
    print(ans)

if __name__ == '__main__':
    main()