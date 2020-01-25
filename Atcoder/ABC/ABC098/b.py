def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        tmpcount = 0
        tmp1 = list(set(S[:i]))
        tmp2 = list(set(S[i:]))
        for j in range(len(tmp1)):
            if tmp1[j] in tmp2:
                tmpcount += 1
        if tmpcount >= count:
            count = tmpcount
    print(count)

if __name__ == '__main__':
    main()