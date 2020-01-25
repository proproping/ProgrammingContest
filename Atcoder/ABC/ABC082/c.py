def main():
    from collections import Counter
    N = int(input())
    a = list(map(int,input().split()))
    count = Counter(a)
    a = list(set(a))
    ans = 0
    for i in a:
        if count[i] >= i:
            ans += count[i]-i
        else:
            ans += count[i]
    print(ans)

if __name__ == '__main__':
    main()