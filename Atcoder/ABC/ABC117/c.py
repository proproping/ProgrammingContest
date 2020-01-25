def main():
    N,M = map(int,input().split())
    X = sorted(list(map(int,input().split())))
    if N >= M:
        print(0)
    else:
        gap = []
        for i in range(M-1):
            gap.append(abs(X[i+1]-X[i]))
        gap = sorted(gap,reverse = 1)
        print(sum(gap[N-1:]))

if __name__ == '__main__':
    main()