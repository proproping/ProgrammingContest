def main():
    a,b = map(int,input().split())
    if a > 0:
        if b > 0:
            print("Positive")
        else:
            print("Zero")
    else:
        if b >= 0:
            print("Zero")
        else:
            if (a-b)%2 == 0:
                print("Negative")
            else:
                print("Positive")

if __name__ == '__main__':
    main()