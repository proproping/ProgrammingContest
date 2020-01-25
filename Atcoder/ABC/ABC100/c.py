def main():
    N = int(input())
    a = list(map(int,input().split()))
    tmp = []
    for i in range(N):
        if a[i]%2 == 0:
            tmp.append(a[i])
    if tmp == []:
        print(0)
    else:
        ans = 0
        for i in range(len(tmp)):
            num = tmp[i]
            count = 0
            while num%2 == 0:
                num = num/2
                count += 1
            ans += count
        print(ans)

if __name__ == '__main__':
    main()