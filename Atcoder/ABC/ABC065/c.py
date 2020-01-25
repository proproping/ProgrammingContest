def main():
    import math
    mod = 10**9+7
    N,M = map(int,input().split())
    if abs(N-M) > 1:
        print(0)
    elif N == M:
        print((math.factorial(N)*math.factorial(M)*2)%mod)
    else:
        print((math.factorial(N)*math.factorial(M))%mod)

if __name__ == '__main__':
    main()