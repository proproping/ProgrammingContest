def main():
    W,H,N = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(N)]
    tmp = [0]*W
    tmp = [tmp]*H
    for i in range(N):
        if mat[i][2] == 1:
            for j in range(H):
                for k in range(mat[i][0]):
                    tmp[j][k] = 1
        elif mat[i][2] == 2:
            for j in range(H):
                for k in range(mat[i][0],W):
                    tmp[j][k] = 1
        elif mat[i][2] == 3:
            for j in range(0,mat[i][1]):
                tmp[j] = [1]*W
        else:
            for j in range(mat[i][1],H):
                tmp[j] = [1]*W
    print(max([W*H-sum(list(map(sum,tmp))),0]))

if __name__ == '__main__':
    main()