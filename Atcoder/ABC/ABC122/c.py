def main():
    N,Q = map(int,input().split())
    S = input()
    ac = [0]*(N+1)
    for i in range(N):
        ac[i+1] = ac[i] + (1 if S[i:i+2] == "AC" else 0)
    for i in range(Q):
        l,r = map(int,input().split())
        print(ac[r-1]-ac[l-1])

if __name__ == '__main__':
    main()