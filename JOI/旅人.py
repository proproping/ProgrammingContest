from itertools import accumulate

def main():
    ans = 0
    n, m = map(int,input().split())
    cost = [int(input()) for _ in range(n - 1)]
    q = [int(input()) for _ in range(m)]
    cumsum = list(accumulate(cost))
    cumsum.insert(0,0)
    index = 0
    for i in range(m):
        ans += abs(cumsum[index] - cumsum[index + q[i]])
        index += q[i]
    print(ans % 10 ** 5)

if __name__ == '__main__':
    main()