def main():
    n = int(input())
    m = int(input())
    friends = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        friends[a - 1].append(b-1)
        friends[b - 1].append(a - 1)
    tmp = [x for x in friends[0]]
    for i in friends[0]:
        for j in friends[i]:
            if j != 0:
                tmp.append(j)
    ans = len(set(tmp))
    print(ans)

if __name__ == '__main__':
    main()