def main():
    N = int(input())
    T = list(map(int,input().split()))
    M = int(input())
    mat = [list(map(int,input().split())) for i in range(M)]
    ans = [0]*M
    time = sum(T)
    for i in range(M):
        ans[i] = time-T[mat[i][0]-1]+mat[i][1]
    for j in range(len(ans)):
        print(ans[j])

if __name__ == '__main__':
    main()