def main():
    N,M = map(int,input().split())
    sw = []
    for i in range(M):
        tmp = list(map(int,input().split()))
        sw.append(tmp[1:])
    p = list(map(int,input().split()))
    bit = []
    for i in range(2**N):
        tmp = list(map(int,bin(i)[2:].zfill(N)))
        bit.append(tmp)
    ans = 0
    for i in range(2**N):
        all = True
        for j in range(M):
            num = 0
            for k in range(len(sw[j])):
                if bit[i][sw[j][k]-1] == 1:
                    num += 1
            if num%2 != p[j]:
                all = False
                break
        ans += all
    print(ans)

if __name__ == '__main__':
    main()