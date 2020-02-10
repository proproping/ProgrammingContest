def main():
    N,K = map(int,input().split())
    modzero = 0
    modhalf = 0
    for i in range(1,N+1):
        if i%K == 0:
            modzero += 1
        elif (i%K == (K/2)) and (K/2 == K//2):
            modhalf += 1
    ans = modzero**3 + modhalf**3
    print(ans)

if __name__ == '__main__':
    main()