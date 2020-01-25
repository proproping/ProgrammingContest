def main():
    import math
    A,B,X = map(int,input().split())
    N = 1
    if A*N+B >= X:
        print(0)
    else:
        N = math.ceil(X/A)
        N = math.ceil(N - (B/A)*len(str(N)))
        if A*N + B*(len(list(str(N)))) > X:
            while A*N + B*(len(list(str(N)))) > X:
                N += -1
            if N > 10**9:
                print(10**9)
            else:
                print(N)
        else:
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**9
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**9
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**8
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**8
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**7
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**7
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**6
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**6
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**5
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**5
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**4
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**4
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**3
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**3
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**2
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**2
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**1
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**1
            while A*N + B*(len(list(str(N)))) < X:
                N += 10**0
            while A*N + B*(len(list(str(N)))) > X:
                N += -10**0
            if N > 10**9:
                print(10**9)
            else:
                print(N)

if __name__ == '__main__':
    main()