ans = - 10**9
n = 0
mat = 0

def dfs(i,v):
    global ans
    if i == n:
        tmp = 0
        for j in range(n):
            for k in range(j+1,n):
                if v[j] == v[k]:
                    tmp += mat[j][k]
        ans = max(ans,tmp)
        return
    else:
        for j in range(3):
            tmp = v
            tmp[i] = j
            dfs(i+1,tmp)

def main():
    global n,mat
    n = int(input())
    mat = [[0]*n for _ in range(n)]
    for i in range(n-1):
        tmp = list(map(int,input().split()))
        for j in range(i+1,n):
            mat[i][j] = tmp[j-i-1]
            mat[j][i] = tmp[j-i-1]
    v = [0]*n
    dfs(0,v)
    print(ans)


if __name__ == '__main__':
    main()