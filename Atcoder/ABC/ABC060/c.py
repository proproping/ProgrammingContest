def main():
    N,T = map(int,input().split())
    t = list(map(int,input().split()))
    count = 0
    for i in range(1,N):
        if t[i-1] + T > t[i]:
            count += t[i-1] + T - t[i]
    print(N*T-count)

if __name__ == '__main__':
    main()