def main():
    s = input()
    sd = s[::-1]
    n = len(s)
    flag = True
    for i in range(n):
        if (s[i] != sd[i]) and (s[i] != '*') and (sd[i] != '*'):
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")



if __name__ == '__main__':
    main()