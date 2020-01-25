def main():
    t = int(input())
    ans = []
    for i in range(t):
        a,b,c,n = map(int,input().split())
        needcoin = 3*max(a,b,c) - sum([a,b,c])
        if n >= needcoin:
            if (n-needcoin)%3 == 0:
                ans.append("YES")
            else:
                ans.append("NO")
        else:
            ans.append("NO")
    print(*ans,sep="\n")

if __name__ == '__main__':
    main()