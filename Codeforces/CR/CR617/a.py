def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        evenCount = 0
        oddCount = 0
        for j in range(n):
            if a[j]%2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        ans = "NO"
        if oddCount != 0:
            if oddCount%2 != 0:
                ans = "YES"
            elif evenCount != 0:
                ans = "YES"
        print(ans)

if __name__ == '__main__':
    main()