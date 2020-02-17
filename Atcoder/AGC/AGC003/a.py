def main():
    S = list(input())
    nf,wf,sf,ef = False,False,False,False
    for i in range(len(S)-1):
        if S[i] == "N":
            if sf:
                sf = False
            else:
                nf = True
        elif S[i] == "W":
            if ef:
                ef = False
            else:
                wf = True
        elif S[i] == "S":
            if nf:
                nf = False
            else:
                sf = True
        else:
            if wf:
                wf = False
            else:
                ef = True
    if nf or wf or sf or ef:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()