def main():
    N,T = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(N)]
    for i in range(N):
        if mat[i][1] > T:
            mat[i][0] = 1001
    ans = min([x[0] for x in mat])
    if ans == 1001:
        print("TLE")
    else:
        print(ans)

if __name__ == '__main__':
    main()