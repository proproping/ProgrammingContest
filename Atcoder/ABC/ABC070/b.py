def main():
    A,B,C,D = map(int,input().split())
    alice = set(list(range(A,B+1)))
    bob = set(list(range(C,D+1)))
    if list(alice&bob) == []:
        print(0)
    else:
        print(len(alice&bob)-1)

if __name__ == '__main__':
    main()