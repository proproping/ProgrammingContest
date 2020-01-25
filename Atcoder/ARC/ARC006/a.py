def main():
    E = set(map(int,input().split()))
    B = set([int(input())])
    L = set(map(int,input().split()))
    mn = len(L - E)
    if mn >= 4:
        print(0)
    elif mn == 0:
        print(1)
    elif mn == 1:
        print(len(L-E-B)+2)
    else:
        print(mn+2)

if __name__ == '__main__':
    main()