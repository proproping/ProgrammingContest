def main():
    A = [list(map(int,input().split())) for _ in range(3)]
    N = int(input())
    b = [int(input()) for _ in range(N)]
    bng = [[False]*3 for _ in range(3)]
    ans = "No"
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if b[i] == A[j][k]:
                    bng[j][k] = True
    if (bng[0] == [True]*3 or
        bng[1] == [True]*3 or
        bng[2] == [True]*3 or
        bng[0][0] == bng[1][0] == bng[2][0] == True or
        bng[0][1] == bng[1][1] == bng[2][1] == True or
        bng[0][2] == bng[1][2] == bng[2][2] == True or
        bng[0][0] == bng[1][1] == bng[2][2] == True or
        bng[0][2] == bng[1][1] == bng[2][0] == True):
        ans = "Yes"
    print(ans)


if __name__ == '__main__':
    main()