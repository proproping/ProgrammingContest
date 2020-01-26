

def main():
    from operator import itemgetter
    import math
    H,N = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    cp = [AB[i][0]/AB[i][1] for i in range(N)]
    AB = sorted([[AB[i][0],AB[i][1],cp[i]] for i in range(N)],key=itemgetter(1))
    AB = sorted(AB,key=itemgetter(2),reverse=True)
    if AB[0][0] >= H:
        AB = sorted(AB,key=itemgetter(1))
        for i in range(N):
            if H <= AB[i][0]:
                print(AB[i][1])
    else:
        for i in range(N):
            ans += (math.floor(H/AB[i][0]))*AB[i][1]
            H -= (math.floor(H/AB[i][0]))*AB[i][0]
            if H <= 0:
                break
        if H <= 0:
            print(ans)
        else:
            AB = sorted(AB,key=itemgetter(1))
            for i in range(N):
                if H <= AB[i][0]:
                    ans += AB[i][1]
                    break
            print(ans)



if __name__ == '__main__':
    main()