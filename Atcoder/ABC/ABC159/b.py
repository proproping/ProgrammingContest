def main():
    S = input()
    ans = "Yes"
    N = len(S)
    tmp1 = S[: (N - 1) // 2]
    tmp2 = S[(N + 3) // 2 - 1 :]
    if S != S[::-1]:
        ans = "No"
    elif tmp1 != tmp1[::-1]:
        ans = "No"
    elif tmp2 != tmp2[::-1]:
        ans = "No"
    print(ans)

if __name__ == '__main__':
    main()