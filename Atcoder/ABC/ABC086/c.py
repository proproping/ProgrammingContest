def main():
    N = int(input())
    txy = []
    for i in range(N):
        txy.append(list(map(int,input().split())))
    ans = "Yes"
    t = 0
    x = 0
    y = 0
    for i in range(N):
        deft = txy[i][0] - t
        defx = abs(txy[i][1] - x)
        defy = abs(txy[i][2] - y)
        t = txy[i][0]
        x = txy[i][1]
        y = txy[i][2]
        if (defx + defy) > deft:
            ans = "No"
            break
        elif (deft - defx - defy)%2 != 0:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()