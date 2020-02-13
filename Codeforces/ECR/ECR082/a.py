def main():
    t = int(input())
    for i in range(t):
        s = 0
        e = 0
        S = list(input())
        for j in range(len(S)):
            if S[j] == "1":
                s = j
                break
        for j in range(len(S)-1,-1,-1):
            if S[j] == "1":
                e = j
                break
        ans = 0
        for j in range(s,e):
            if S[j] == "0":
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()