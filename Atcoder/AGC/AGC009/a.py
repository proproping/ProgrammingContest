def main():
    N = int(input())
    A = [None]*N
    B = [None]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    ans = 0
    for i in range(N-1,-1,-1):
        if (A[i]+ans)%B[i] == 0:
            continue
        ans += (B[i] - (A[i]+ans)%B[i])
    print(ans)

if __name__ == '__main__':
    main()