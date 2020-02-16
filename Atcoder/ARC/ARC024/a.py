from collections import Counter
def main():
    L,R = map(int,input().split())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    lc = Counter(l)
    ans = 0
    for i in range(R):
        if lc[r[i]] > 0:
            ans += 1
            lc[r[i]] -= 1
    print(ans)

if __name__ == '__main__':
    main()