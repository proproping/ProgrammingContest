def main():
    s = input()
    t = input()
    dp = [[0]*(len(s)+1) for _ in range((len(t)+1))]
    ans = ""
    for i in range(len(t)):
        for j in range(len(s)):
            tmp1 = dp[i+1][j]
            tmp2 = dp[i][j+1]
            tmp3 = dp[i][j]
            if t[i] == s[j]:
                tmp3 += 1
            dp[i+1][j+1] = max(tmp1,tmp2,tmp3)
    i = len(t)
    j = len(s)
    # for k in range(10**6):
    #     if i < 0 or j < 0:
    #         break
    #     if dp[i-1][j-1]+1 == dp[i][j] and t[i-1] == s[j-1]:
    #         ans += t[i-1]
    #         i -= 1
    #         j -= 1
    #     elif dp[i-1][j] == dp[i][j]:
    #         i -= 1
    #     else:
    #         j -= 1
    while i > 0 and j > 0:
        if dp[i-1][j-1]+1 == dp[i][j] and t[i-1] == s[j-1]:
            ans += t[i-1]
            i -= 1
            j -= 1
        elif dp[i-1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1
    print(ans[::-1])


if __name__ == '__main__':
    main()