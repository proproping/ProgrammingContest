def main():
    N,A,B = map(int,input().split())
    print(max((B*(N-1)+A)-(A*(N-1)+B)+1,0))

if __name__ == '__main__':
    main()