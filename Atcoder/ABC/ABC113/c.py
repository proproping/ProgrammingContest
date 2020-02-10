from operator import itemgetter
def main():
    N,M = map(int,input().split())
    py = [list(map(int,input().split())) for _ in range(M)]
    [py[i].append(i) for i in range(M)]
    py = sorted(py,key=itemgetter(1))
    py = sorted(py,key=itemgetter(0))
    now = 0
    num = 1
    ans = []
    for i in range(M):
        if now != py[i][0]:
            now = py[i][0]
            num = 1
        else:
            num += 1
        tmp = str(now).zfill(6)+str(num).zfill(6)
        ans.append([tmp,py[i][2]])
    ans = sorted(ans,key=itemgetter(1))
    for i in range(M):
        print(ans[i][0])


if __name__ == '__main__':
    main()