def main():
    import itertools
    N = int(input())
    d = list(map(int,input().split()))
    tmp = list(itertools.combinations(d,2))
    ans = 0
    for i in range(len(tmp)):
        ans = ans + (tmp[i][0] * tmp[i][1])
    print(ans)

if __name__ == '__main__':
    main()