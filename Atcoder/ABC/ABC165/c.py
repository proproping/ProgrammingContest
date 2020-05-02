def main():
    n, m, q = map(int, input().split())
    integers = [list(map(int, input().split())) for _ in range(q)]
    ans = 0
    for i in range(m):
        for j in range(i, m):
            for k in range(j, m):
                for l in range(k, m):
                    

if __name__ == '__main__':
    main()