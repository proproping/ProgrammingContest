def main():
    s = list(input())
    a = list()
    b = list()
    c = list()
    a.append(s[0])
    for i in range(1,4):
        if s[i] == a[0]:
            a.append(s[i])
        elif len(b) == 0:
            b.append(s[i])
        elif s[i] == b[0]:
            b.append(s[i])
        else:
            c.append(s[i])
    if (len(a) == 2) and (len(b) == 2):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()