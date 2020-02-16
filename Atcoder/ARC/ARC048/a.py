def main():
    A,B = map(int,input().split())
    add = 0
    if A < 0 and B > 0:
        add = 1
    print(B-A-add)

if __name__ == '__main__':
    main()