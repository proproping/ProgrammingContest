def main():
    N = int(input())
    c = [[0]*10 for _ in range(10)]
    for k in range(1,N+1):
        tmp = str(k)
        i = int(tmp[0])
        j = int(tmp[-1])
        c[i][j] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += c[i][j] * c[j][i]
    print(ans)

if __name__ == '__main__':
    main()