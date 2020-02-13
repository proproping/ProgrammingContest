def main():
    N = int(input())
    C = [0]*N
    S = [0]*N
    F = [0]*N
    for i in range(N-1):
        C[i],S[i],F[i] = map(int,input().split())
    for i in range(N):
        t = 0
        for j in range(i,N-1):
            if t < S[j]:
                t = S[j]
            elif t%F[j] != 0:
                t += F[j] - t%F[j]
            t += C[j]
        print(t)

if __name__ == '__main__':
    main()