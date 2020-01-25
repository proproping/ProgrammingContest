def main():
    X = input()
    if X[0] not in ["c","o","k","u"]:
        print("NO")
    else:
        flag = 1
        for i in range(1,len(list(X))):
            if X[i-1] == "c":
                if X[i] not in ["h","o","k","u"]:
                    print("NO")
                    flag = 0
                    break
            else:
                if X[i] not in ["o","k","u"]:
                    print("NO")
                    flag = 0
                    break
        if flag == 1:
            print("YES")

if __name__ == '__main__':
    main()