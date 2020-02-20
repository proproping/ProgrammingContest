def main():
    N = int(input())
    A = list(map(int,input().split()))
    before = A[0]
    count = 0
    upflag = False
    downflag = False
    for i in range(1,N):
        if upflag:
            if A[i] - before < 0:
                upflag = False
                downflag = False
        elif downflag:
            if A[i] - before > 0:
                downflag = False
                upflag = False
        else:
            if A[i] - before > 0:
                upflag = True
                count += 1
            elif A[i] - before < 0:
                downflag = True
                count += 1
        before = A[i]
    if not (upflag or downflag):
        count += 1
    print(count)

if __name__ == '__main__':
    main()