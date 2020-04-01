import heapq

def main():
    x, y, a, b, c = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    p = [p[i] for i in range(-x, 0)]
    q = sorted(list(map(int, input().split())))
    q = [q[i] for i in range(-y, 0)]
    r = sorted(list(map(int, input().split())), reverse=True)
    for i in range(c):
        red = heapq.heappop(p)
        green = heapq.heappop(q)
        if r[i] <= red and r[i] <= green:
            heapq.heappush(p, red)
            heapq.heappush(q,green)
            break
        else:
            if r[i] - red >= r[i] - green:
                heapq.heappush(p, r[i])
                heapq.heappush(q,green)
            else:
                heapq.heappush(q, r[i])
                heapq.heappush(p, red)
    print(sum(p)+sum(q))

if __name__ == '__main__':
    main()