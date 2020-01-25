def main():
    import numpy as np
    H,W = map(int,input().split())
    mat = [(list(input())) for _ in range(H)]
    L = [[0]*W for _ in range(H)]
    R = [[0]*W for _ in range(H)]
    D = [[0]*W for _ in range(H)]
    U = [[0]*W for _ in range(H)]

    for i in range(H):
        for j in range(W-1):
            if mat[i][j] != "#":
                if j == 0:
                    L[i][j] = 1
                else:
                    L[i][j] = L[i][j-1]+1
            else:
                L[i][j] = 0
    for i in range(H):
        for j in range(W-1,-1,-1):
            if mat[i][j] != "#":
                if j == (W-1):
                    R[i][j] = 1
                else:
                    R[i][j] = R[i][j+1]+1
            else:
                R[i][j] = 0
    for i in range(H-1,-1,-1):
        for j in range(W):
            if mat[i][j] != "#":
                if i == (H-1):
                    D[i][j] = 1
                else:
                    D[i][j] = D[i+1][j]+1
            else:
                D[i][j] = 0
    for i in range(H-1):
        for j in range(W):
            if mat[i][j] != "#":
                if i == 0:
                    U[i][j] = 1
                else:
                    U[i][j] = U[i-1][j]+1
            else:
                U[i][j] = 0
    ans = 0
    for i in range(H):
        for j in range(W):
            tmp = L[i][j]+R[i][j]+D[i][j]+U[i][j]-3
            if ans < tmp:
                ans = tmp
    print(ans)

if __name__ == '__main__':
    main()