def main():
    H,W = map(int,input().split())
    v = [[] for _ in range(H*W)]
    A = [list(map(int,input().split())) for _ in range(H)]
    dx = [-1,-1,0]
    dy = [1,0,1]
    for i in range(H):
        for j in range(W):
            for k in range(3):
                if 0 <= i-dy[k] and 0 <= j+dx[k]:
                    if k == 0:
                        ti,tj = -1,-1
                    elif k == 1:
                        ti,tj = -1,0
                    else:
                        ti,tj = 1,-1
                    v[i*W+j].append([i*W+j,A[i-dy[k]][i+dx[k]]])
    print(v)



if __name__ == '__main__':
    main()