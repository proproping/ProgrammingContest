from collections import deque

def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(N)]
    mat = [[-1]*N for _ in range(N)]
    mat[0][0] = "R"
    mat[0][N-1] = "B"
    mat[N-1][0] = "G"
    mat[N-1][N-1] = "Y"
    R = deque([[0,0]])
    B = deque([[0,N-1]])
    G = deque([[N-1,0]])
    Y = deque([[N-1,N-1]])
    for i in range(M//4):
        popleft

if __name__ == '__main__':
    main()