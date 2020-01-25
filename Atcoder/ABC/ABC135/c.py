def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        cankill = B[i]
        ans += min([A[i],B[i]])
        if B[i] - A[i] > 0:
            additional = min([B[i] - A[i],A[i+1]])
            ans += additional
            A[i+1] += - additional
    print(ans)

if __name__ == '__main__':
    main()