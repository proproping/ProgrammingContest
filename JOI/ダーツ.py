from itertools import product
from bisect import bisect_left

def main():
    N, M = map(int, input().split())
    p = [int(input()) for _ in range(N)]
    p.append(0)
    points = []
    for i in range(N + 1):
        for j in range(i, N + 1):
            points.append(p[i] + p[j])
    points.sort()
    ans = 0
    for i in range(len(points)):
        index = bisect_left(points, M - points[i])
        if index != 0:
            ans = max(ans, points[i] + points[index - 1])
    print(ans)


if __name__ == '__main__':
    main()