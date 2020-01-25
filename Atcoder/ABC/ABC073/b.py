def main():
    N = int(input())
    mat = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(len(mat)):
        ans += len(list(range(mat[i])))
    print(ans)

if __name__ == '__main__':
    main()