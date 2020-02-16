def main():
    A = [list(map(int,input().split())) for _ in range(4)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    flag = False
    for i in range(4):
        if flag:
            break
        for j in range(4):
            if flag:
                break
            for k in range(4):
                if 0 <= i+dy[k] < 4 and 0 <= j+dx[k] < 4:
                    if A[i][j] == A[i+dy[k]][j+dx[k]]:
                        flag = True
                        break
    if flag:
        print("CONTINUE")
    else:
        print("GAMEOVER")

if __name__ == '__main__':
    main()