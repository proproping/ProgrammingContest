def main():
    A,B,C = map(int,input().split())
    if A >= C or B >= C or A+B >= C:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()