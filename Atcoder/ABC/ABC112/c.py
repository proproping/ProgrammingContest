from operator import itemgetter
def main():
    N = int(input())
    xyh = sorted([list(map(int,input().split())) for _ in range(N)],key=itemgetter(2),reverse = True)
    for px in range(101):
        for py in range(101):
            X,Y,H = xyh[0][0],xyh[0][1],xyh[0][2]
            ph = H + abs(X-px) + abs(Y-py)
            for i in range(N):
                X,Y,H = xyh[i][0],xyh[i][1],xyh[i][2]
                tmp = max(ph - abs(X-px) - abs(Y-py),0)
                if tmp != H:
                    break
                if i == N-1:
                    print(px,py,ph)



if __name__ == '__main__':
    main()