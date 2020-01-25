def main():
    N = int(input())
    T = [[] for _ in range(N)]
    for i in range(N):
        A = int(input())
        for j in range(A):
            T[i].append(list(map(int,input().split())))
    S = [[-1] for _ in range(N)]
    tmp = list(range(2**N-1,-1,-1))
    bins = [format(tmp[i],"0b").zfill(N) for i in range(2**N)]
    for i in range(2**N):
        for j in range(N):
            if bins[i][j] == 1:
                for k in range(len(T[i])):
                    if S[T[i][k][0]-1] != -1 and S[T[i][k][0]-1] != T[i][k][1]:
                        break
                    else:
                        S[T[i][k][0]-1] = T[i][k][1]

if __name__ == '__main__':
    main()