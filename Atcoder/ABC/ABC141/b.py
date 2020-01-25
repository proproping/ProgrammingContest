def main():
    a = list(str(input()))
    odd = a[0::2]
    even = a[1::2]
    if ("L" not in odd) and ("R" not in even):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()