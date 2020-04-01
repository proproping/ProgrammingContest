from collections import defaultdict
INF = float('inf')
def main():
    N, X, Y = map(int, input().split())
    d = defaultdict(lambda: 0)
    for i in range(1,N+1):
        for j in range(1, N + 1):
            if i < j:
                dist = min(min(abs(j - i), abs(X - i) + 1 + abs(j - Y)), abs(Y - i) + 1 + abs(j - X))
                d[dist] += 1
    for i in range(1, N):
        print(d[i])

if __name__ == '__main__':
    main()