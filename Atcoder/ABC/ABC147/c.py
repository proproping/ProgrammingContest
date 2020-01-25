def main():
    N = int(input())
    mat = []
    zero = []
    for i in range(N):
        A = int(input())
        tmp = [list(map(int,input().split())) for _ in range(A)]
        mat.append(tmp)
    ans = N
    num = list(range(1,N+1))
    flag = [[[] for _ in range(2)] for _ in range(N)]
    dic = dict(zip(num,flag))
    count = 1
    for i in mat:
        for j in range(len(i)):
            dic[i[j][0]][0].append(count)
            dic[i[j][0]][1].append(i[j][1])
        count += 1
    tmp = list(dic.values())
    pres = []
    for i in range(len(tmp)):
        if tmp[i][0] == []:
            pres.append(i+1)
    for i in range(len(pres)):
        for j in range(len(tmp)):
            for k in range(len(tmp[j][0])):
                if tmp[j][0][k] == pres[i] and tmp[j][1][k] == 0:
                    tmp[j][1][k] = 1
                    ans += -1
    for i in range(len(tmp)):
        if 0 in tmp[i][1] and 1 in tmp[i][1]:
            ans += -1
    for i in range(len(tmp)):
        if 1 in tmp[i][1] or tmp[i][1] == []:
            break
        else:
            if i == len(tmp)-1:
                ans += -1
    print(ans)

if __name__ == '__main__':
    main()