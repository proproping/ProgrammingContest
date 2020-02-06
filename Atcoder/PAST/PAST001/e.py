def main():
    N,Q = map(int,input().split())
    S = []
    for i in range(Q):
        S.append(list(map(int,input().split())))
    mat = [[False]*N for _ in range(N)]
    for i in S:
        if i[0] == 1:
            mat[i[1]-1][i[2]-1] = True
        elif i[0] == 2:
            for j in range(N):
                if mat[j][i[1]-1]:
                    mat[i[1]-1][j] = True
        else:
            tmp = []
            for j in range(N):
                if mat[i[1]-1][j]:
                    tmp.append(j)
            for j in tmp:
                for k in range(N):
                    if mat[j][k] and k != i[1]-1:
                        mat[i[1]-1][k] = True
    for i in range(N):
        for j in range(N):
            if mat[i][j]:
                mat[i][j] = "Y"
            else:
                mat[i][j] = "N"
    for i in range(N):
        print(*mat[i],sep="")


if __name__ == '__main__':
    main()