import itertools
def main():
    N = int(input())
    if N < 357:
        print(0)
    else:
        digit = 1
        n = N
        while N//10 != 0:
            N //= 10
            digit += 1
        ans = 0
        for i in range(3,digit+1):
            ls = list(itertools.product([3,5,7],repeat=i))
            for j in ls:
                if 3 in j and 5 in j and 7 in j:
                    tmp = 0
                    for k in range(1,len(j)+1):
                        tmp += j[-k]*10**(k-1)
                    if tmp <= n:
                        ans += 1
        print(ans)


if __name__ == '__main__':
    main()