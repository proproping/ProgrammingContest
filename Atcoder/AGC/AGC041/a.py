def main():
    N,A,B = map(int,input().split())
    if (A-B)%2 == 0:
        print(abs((A-B)//2))
    elif A == 1 or B == N:
        print((abs(A-B)-1)//2+1)
    else:
        which = min((A-1),N-B)
        if which == A-1:
            count = A-1+1
            A = 1
            B -= count
            print(abs(A-B)//2+count)
        else:
            count = N-B+1
            A += count
            B = N
            print(abs(A-B)//2+count)

if __name__ == '__main__':
    main()