def main():
    import numpy as np
    from fractions import gcd
    N,X = map(int,input().split())
    x = np.array(list(map(int,input().split())))-X
    ans = x[0]
    for i in range(1,N):
        ans = gcd(ans,x[i])
    print(abs(ans))

if __name__ == '__main__':
    main()