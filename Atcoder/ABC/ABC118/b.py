def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(N)]
    K = []
    for i in range(N):
        K.append(A[i].pop(0))
    ans = A[0]
    for j in range(1,N):
        ans = set(ans)&set(A[j])
    print(len(ans))

if __name__ == '__main__':
    main()