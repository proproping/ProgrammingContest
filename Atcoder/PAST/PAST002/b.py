from collections import Counter

def main():
    s = list(input())
    c = Counter(s)
    maxvote = max(c.values())
    ans = ""
    for key in c.keys():
        if c[key] == maxvote:
            ans = key
    print(ans)

if __name__ == '__main__':
    main()