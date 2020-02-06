def main():
    N = int(input())
    mat = [[0]*N for _ in range(N)]
    for i in range(N-1):
        tmp = list(map(int,input().split()))
        for j in range(len(tmp)):
            mat[i][j] = tmp[j]

if __name__ == '__main__':
    main()