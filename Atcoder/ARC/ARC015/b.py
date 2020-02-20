def main():
    N = int(input())
    ans = [0]*6
    for i in range(N):
        MT,mT = map(float,input().split())
        if MT >= 35:
            ans[0] += 1
        if 30 <= MT < 35:
            ans[1] += 1
        if 25 <= MT < 30:
            ans[2] += 1
        if mT >= 25:
            ans[3] += 1
        if mT < 0 and MT >= 0:
            ans[4] += 1
        if MT < 0:
            ans[5] += 1
    print(*ans,sep=" ")

if __name__ == '__main__':
    main()