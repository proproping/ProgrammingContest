def main():
    S = input()
    iflag = False
    cflag = False
    tflag = False
    for i in range(len(S)):
        if (not iflag) and (S[i] == "i" or S[i] == "I"):
            iflag = True
        elif (iflag) and (S[i] == "c" or S[i] == "C"):
            cflag = True
        elif (cflag) and (S[i] == "t" or S[i] == "T"):
            tflag = True
    if iflag and cflag and tflag:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()