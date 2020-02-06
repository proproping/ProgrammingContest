def main():
    S = str(input())
    words = []
    UFlag = False
    tmp = ""
    for i in range(len(S)):
        tmp += S[i]
        if UFlag and S[i].isupper():
            words.append(tmp)
            UFlag = False
            tmp = ""
        elif S[i].isupper():
            UFlag = True
    print(*sorted(words,key=str.lower),sep="")

if __name__ == '__main__':
    main()