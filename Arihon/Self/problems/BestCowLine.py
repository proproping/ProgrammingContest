def main():
    N = int(input())
    S = input()
    T = ""
    for i in range(N):
        ST = S[::-1]
        if S < ST:
            T += S[0]
            S = S[1:]
        else:
            T += S[-1]
            S = S[:-1]
    print(T)


if __name__ == '__main__':
    main()

"""
in
6
ACDBCB
"""