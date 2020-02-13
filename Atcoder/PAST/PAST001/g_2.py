import itertools
INF = 10**9

def main():
    n = int(input())
    mat = [[0]*n for _ in range(n)]
    for i in range(n-1):
        tmp = list(map(int,input().split()))
        for j in range(i+1,n):
            mat[i][j] = tmp[j-i-1]
            mat[j][i] = tmp[j-i-1]
    ls = list(itertools.product([0,1,2],repeat=n))
    ans = - INF
    for i in range(len(ls)):
        tmp = 0
        comb = ls[i]
        for j in range(n):
            for k in range(j+1,n):
                if comb[j] == comb[k]:
                    tmp += mat[j][k]
        ans = max(ans,tmp)
    print(ans)


if __name__ == '__main__':
    main()