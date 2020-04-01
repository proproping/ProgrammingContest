INF = float('inf')

def main():
    H,W = map(int,input().split())
    mat = [list(input()) for _ in range(H)]
    dp = []
    print(*mat,sep="\n")

if __name__ == '__main__':
    main()