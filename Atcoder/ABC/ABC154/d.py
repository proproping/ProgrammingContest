def DE(n):
    return float((float(n)+1)/2)

def main():
    N,K = map(int,input().split())
    p = list(map(DE,input().split()))
    ans = 0
    tmp = [sum(p[:K])]
    for i in range(K,N):
        tmp.append(tmp[i-K]+p[i]-p[i-K])
    print(max(tmp))

if __name__ == '__main__':
    main()