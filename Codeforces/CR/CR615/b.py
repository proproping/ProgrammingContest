def main():
    from operator import itemgetter
    t = int(input())
    for i in range(t):
        flag = False
        n = int(input())
        xy = [list(map(int,input().split())) for _ in range(n)]
        xy = sorted(xy,key=itemgetter(0))
        xy = sorted(xy,key=itemgetter(1))
        x,y = 0,0
        ans = ""
        for j in xy:
            if j[0]-x < 0 or j[1]-y < 0:
                x = j[0]
                y = j[1]
                flag = True
            else:
                ans += "R"*(j[0]-x)+"U"*(j[1]-y)
                x = j[0]
                y = j[1]
        if flag:
            print("NO")
        else:
            print("YES")
            print(ans)


if __name__ == '__main__':
    main()