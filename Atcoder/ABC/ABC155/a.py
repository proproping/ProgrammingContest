def main():
    A,B,C = map(int,input().split())
    t = set([A,B,C])
    if len(t) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()