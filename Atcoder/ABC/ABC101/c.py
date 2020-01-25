def main():
    import math
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    print(math.ceil((N-1)/(K-1)))

if __name__ == '__main__':
    main()