def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    for i in range(1,N):
        if A[i] == A[i-1]:
            print("stay")
        elif A[i] > A[i-1]:
            print("up",abs(A[i]-A[i-1]))
        else:
            print("down",abs(A[i]-A[i-1]))

if __name__ == '__main__':
    main()