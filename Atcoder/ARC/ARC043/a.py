def main():
    N,A,B = map(int,input().split())
    S = [int(input()) for _ in range(N)]
    if len(set(S)) == 1:
        print(-1)
    else:
        mins = min(S)
        maxs = max(S)
        aves = sum(S)/N
        P = B/(maxs-mins)
        Q = A-(aves*P)
        print(P,Q)

if __name__ == '__main__':
    main()