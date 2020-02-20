def main():
    x,y = map(int,input().split())
    ans = abs(abs(x) - abs(y))
    if x == 0 or y == 0:
        ans = max(list(map(abs,[x,y])))
        if x < 0 or y < 0:
            ans += 1
    elif abs(x) <= abs(y):
        if x*y < 0:
            ans += 1
        if x < 0 and y < 0:
            ans += 2
    else:
        if x*y < 0:
            ans += 1
        if x > 0 and y > 0:
            ans += 2
    print(ans)

if __name__ == '__main__':
    main()