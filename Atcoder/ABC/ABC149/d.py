def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = list(input())
    for i in range(N-K):
        if T[i] == T[i+K]:
            T[i+K] = "@"
    dic1 = {"r":P,"s":R,"p":S,"@":0}
    points = 0
    for i in range(N):
        points += dic1[T[i]]
    print(points)

if __name__ == '__main__':
    main()