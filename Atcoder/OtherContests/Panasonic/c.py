def main():
    a, b, c = map(int, input().split())
    T = (c - a - b)
    if 4*a*b < T**2 and 0 < T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()