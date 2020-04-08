def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    limit = sum(A) / (4 * M)
    count = 0
    for i in range(N):
        if A[i] >= limit:
            count += 1
    if count >= M:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()