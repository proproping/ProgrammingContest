def main():
    s = input()
    t = input()
    tmp1 = "".join(sorted(list(s)))
    tmp2 = "".join(sorted(list(t),reverse = 1))
    if tmp1 < tmp2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()