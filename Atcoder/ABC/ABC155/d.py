def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    nega = sorted([A[i] for i in range(N) if A[i] < 0])
    posi = sorted([A[i] for i in range(N) if A[i] > 0])
    zero = 0
    for i in range(N):
        if A[i] == 0:
            zero += 1
    negan = len(nega)*len(posi)
    zeron = (N-1)*zero
    posin = (N*(N-1)//2) - negan - zeron
    if negan < K <= negan+zeron:
        print(0)
    elif negan >= K:
        tmp = []
        for i in range(len(nega)):
            for j in range(len(posi)):
                tmp.append(nega[i]*posi[j])
        print(sorted(tmp[K-1]))
    else:
        tmp = []
        for i in range(len(nega)):
            for j in range(len(nega)):
                if i != j:
                    tmp.append(nega[i]*nega[j])
        for i in range(len(posi)):
            for j in range(len(posi)):
                if i != j:
                    tmp.append(posi[i]*posi[j])
        tmp.sort()
        print(tmp.index(448283280358331064))
        print(K,negan,zeron)
        print(K-246)


if __name__ == '__main__':
    main()