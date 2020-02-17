def main():
    N = list(input()[::-1])
    n = int("".join(N[::-1]))
    N = list(map(int,N))
    N.append(0)
    num = []
    for i in range(len(N)):
        if N[i] >= 10:
            N[i+1] += 1
            N[i] = N[i]%10
        if N[i] > 5:
            N[i+1] += 1
            num.append("0")
        else:
            num.append(str(N[i]))
    ans = sum(list(map(int,num[::-1])))
    t1 = int("".join(num[::-1]))
    t2 = int(n)
    tmp = sum(list(map(int,list(str(t1-t2)))))
    print(ans+tmp)
    print(int("".join(num[::-1])))

if __name__ == '__main__':
    main()