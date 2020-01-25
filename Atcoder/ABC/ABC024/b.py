def main():
    N,T = map(int,input().split())
    A = [int(input()) for i in range(N)]
    ans = T
    opendoor = 0
    for i in range(N-1):
        if opendoor == 0:
            if A[i]+T <= A[i+1]:
                ans += T
            else:
                openstart = i
                opendoor = 1
        else:
            if A[i]+T <= A[i+1]:
                ans += (A[i]+T) - A[openstart]
                openstart = N-1
                opendoor = 0
    ans += A[N-1] - A[openstart]
    print(ans)

if __name__ == '__main__':
    main()