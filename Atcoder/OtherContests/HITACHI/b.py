def main():
    A,B,M = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = min(a) + min(b)
    coupon = [list(map(int,input().split())) for _ in range(M)]
    for i in range(M):
        tmp = a[coupon[i][0]-1] + b[coupon[i][1]-1] - coupon[i][2]
        ans = min(tmp,ans)
    print(ans)

if __name__ == '__main__':
    main()