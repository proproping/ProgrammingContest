def main():
    N,M,V,P = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    seta = list(set(A))
    count = 0
    tmp = -P+(V)
    if tmp > 0:
        tmp = -1
    for i in range(N):
        if A[i]+M >= A[-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()