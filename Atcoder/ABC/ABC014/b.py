def main():
    import numpy as np
    n,X = map(int,input().split())
    a = np.array(list(map(int,input().split())))
    binaryX = bin(X)[2:]
    binaryX = list(binaryX.zfill(n))
    binaryX.reverse()
    binaryX = np.array(list(map(int,binaryX)))
    ans = sum(list(a*binaryX))
    print(ans)

if __name__ == '__main__':
    main()