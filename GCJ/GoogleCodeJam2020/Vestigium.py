def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        mat = [list(map(int, input().split())) for _ in range(N)]
        K, R, C = 0, 0, 0
        for j in range(N):
            K += mat[j][j]
        for j in range(N):
            if len(set(mat[j])) != N:
                R += 1
        for j in range(N):
            tmp = []
            for k in range(N):
                tmp.append(mat[k][j])
            if len(set(tmp)) != N:
                C += 1
        print("Case #{}: {} {} {}".format(i+1,K,R,C))

if __name__ == '__main__':
    main()