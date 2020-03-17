def main():
    N = int(input())
    R = int(input())
    X = sorted(list(map(int,input().split())))
    i = 0
    ans = 0
    while i < N:
        s = X[i]
        i += 1
        while i < N and X[i] <= s + R:
            i += 1
        p = X[i-1]
        while i < N and X[i] <= p + R:
            i += 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()

"""
in
6
10
1 7 15 20 30 50

out
3
"""