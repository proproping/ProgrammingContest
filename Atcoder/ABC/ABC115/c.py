def main():
    N,K = map(int,input().split())
    h = sorted([int(input()) for i in range(N)])
    tmp = []
    for i in range(N-K+1):
        tmp.append(h[i+K-1]-h[i])
    print(min(tmp))

if __name__ == '__main__':
    main()