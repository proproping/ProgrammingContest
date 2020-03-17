def main():
    n = int(input())
    m = int(input())
    s = input()
    pn = "IOI" + ("OI" * (n-1))
    limit = len(pn)
    searchflag = False
    nextI = False
    tmp = []
    start = 0
    i = 0
    ans = 0
    while i < m:
        if searchflag:
            if not nextI and s[i] == "O":
                nextI = not nextI
            elif nextI and s[i] == "I":
                nextI = not nextI
            else:
                if s[i-1] == "I":
                    searching = s[start:i]
                else:
                    searching = s[start: i - 1]
                i -= 1
                if len(searching) >= limit:
                    tmp.append(searching)
                searchflag = not searchflag
        else:
            if s[i] == "I":
                start = i
                nextI = False
                searchflag = True
        i += 1
    for i in range(len(tmp)):
        ans += len(tmp[i]) // 2 - n + 1
    print(ans)

if __name__ == '__main__':
    main()