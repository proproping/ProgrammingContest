def main():
    S = input()
    if len(S)%2 == 0:
        tmp1 = S[:len(S)//2]
        tmp2 = S[len(S)//2:]
        tmp2 = tmp2[::-1]
        count = 0
        for i in range(len(tmp1)):
            if tmp1[i] != tmp2[i]:
                count += 1
        print(count)
    else:
        tmp1 = S[:len(S)//2]
        tmp2 = S[len(S)//2+1:]
        tmp2 = tmp2[::-1]
        count = 0
        for i in range(len(tmp1)):
            if tmp1[i] != tmp2[i]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()