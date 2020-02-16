def main():
    N,W,K,V = map(int,input().split())
    cv = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N//W):
        for j in range(W):
            print(j)

if __name__ == '__main__':
    main()