def main():
    N,A,B = map(int,input().split())
    if N > 5:
        print(B*5+A*(N-5))
    else:
        print(B*N)

if __name__ == '__main__':
    main()