def main():
    C,c = input().split()
    if str.swapcase(c) == C:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()