def main():
    N = int(input())
    L = sorted(list(map(int,input().split())),reverse=True)
    ans = 0
    tmp = sum(L)
    for i in range(N-1):
        ans += tmp
        tmp -= L[i]
    print(ans)


if __name__ == '__main__':
    main()

"""
in
3
8 5 8

out
34
"""