def main():
    N,M = map(int,input().split())
    sc = [list(map(int,input().split())) for _ in range(M)]
    if M == 0:
        if N != 1:
            print(10**(N-1))
        else:
            print(0)
    else:
        ans = "-1"
        flag = False
        for i in range(10**N):
            if flag:
                break
            tmp = str(i)
            if len(tmp) < N:
                continue
            for j in range(M):
                if tmp[sc[j][0]-1] != str(sc[j][1]):
                    break
                if j == M-1:
                    ans = i
                    flag = True
        print(ans)

if __name__ == '__main__':
    main()
