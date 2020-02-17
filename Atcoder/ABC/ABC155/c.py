from collections import Counter
def main():
    N = int(input())
    S = [input() for _ in range(N)]
    s = list(set(S))
    c = Counter(S)
    maxc = max(c.values())
    ans = []
    for i in range(len(s)):
        if c[s[i]] == maxc:
            ans.append(s[i])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])


if __name__ == '__main__':
    main()