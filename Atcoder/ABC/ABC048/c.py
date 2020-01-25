def main():
    N,x = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(N-1):
        if a[i]+a[i+1] >= x:
            tmp = (a[i]+a[i+1]-x)
            a[i+1] -= tmp
            a[i+1] = max(0,a[i+1])
            count += tmp
    print(count)

if __name__ == '__main__':
    main()