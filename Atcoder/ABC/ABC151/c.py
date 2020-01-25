def main():
    N,M = map(int,input().split())
    dic = dict(zip(list(range(1,N+1)),[0]*N))
    bl = [True]*N
    ac,wa = 0,0
    for i in range(M):
        p,s = input().split()
        if s == "WA":
            dic[int(p)] += 1
        elif s == "AC":
            if bl[int(p)-1]:
                ac += 1
                wa += dic[int(p)]
                bl[int(p)-1] = False
    print(ac,wa)

if __name__ == '__main__':
    main()