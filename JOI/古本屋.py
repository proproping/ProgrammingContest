from collections import defaultdict
import itertools

def main():
    n, k = map(int, input().split())
    books = [[] for _ in range(10)]
    for i in range(n):
        value, key = map(int, input().split())
        books[key - 1].append(-value)
    books = list(map(sorted, books))
    sales = [[0] * (n + 1) for _ in range(10)]
    for i in range(10):
        for j in range(n):
            if j >= len(books[i]):
                break
            sales[i][j + 1] = sales[i][j] + books[i][j] + j * 2
    dp = [[0] * (k + 1) for _ in range(11)]
    for i in range(10):
        for j in range(k + 1):
            for l in range(len(sales[i]) + 1):
                if j + l <= k:
                    dp[i + 1][j + l] = max(dp[i + 1][j + l], dp[i][j] + sales[i][l])
    print(dp[10][k])

if __name__ == '__main__':
    main()