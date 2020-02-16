def main():
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        c = input()
        ans = "YES"
        for j in range(len(a)):
            if c[j] == a[j] or c[j] == b[j]:
                continue
            else:
                ans = "NO"
                break
        print(ans)

if __name__ == '__main__':
    main()