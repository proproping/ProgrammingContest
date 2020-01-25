def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.insert(0,0),A.append(0)
    time = 0
    now = 0
    for i in range(N+2):
        time += abs(A[i]-now)
        now = A[i]
    for i in range(1,N+1):
        if A[i-1] <= A[i] <= A[i+1]:
            print(time)
        else:
            print(time-((abs(A[i-1]-A[i])+abs(A[i]-A[i+1]))-abs(A[i-1]-A[i+1])))

if __name__ == '__main__':
    main()