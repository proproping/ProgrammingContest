def main():
    N = int(input())
    V = list(map(int,input().split()))
    C = list(map(int,input().split()))
    tmp = list()
    for i in range(N):
        if V[i] - C[i] > 0:
            tmp.append(V[i]-C[i])
    print(sum(tmp))

if __name__ == '__main__':
    main()