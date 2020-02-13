import numpy as np
def main():
    N = int(input())
    C = list(map(int,input().split()))
    Q = int(input())
    S = [list(map(int,input().split())) for _ in range(Q)]
    oddC = np.array([C[i] for i in range(N) if i%2 == 0])
    evenC = np.array([C[i] for i in range(N) if i%2 != 0])
    lenodd = len(oddC)
    minoddC = min(oddC)
    minC = min(C)
    oddsale = 0
    holdsale = 0
    ans = 0
    for i in range(Q):
        if S[i][0] == 1:
            t,x,a = map(int,S[i])
            if x%2 != 0:
                # 奇数なら
                if oddC[x//2]-oddsale-holdsale >= a:
                    oddC[x//2] -= a
                    minoddC = min(minoddC,oddC[x//2]-oddsale-holdsale)
                    minC = min(minC,minoddC)
                    ans += a

            else:
                #偶数なら
                if evenC[x//2-1]-holdsale >= a:
                    evenC[x//2-1] -=a
                    minC = min(minC,evenC[x//2-1]-holdsale)
                    ans += a
        elif S[i][0] == 2:
            t,a = map(int,S[i])
            if minoddC >= a:
                minoddC -= a
                minC = min(minC,minoddC)
                oddsale += a
                ans += a*lenodd
        elif S[i][0] == 3:
            t,a = map(int,S[i])
            if minC >= a:
                minoddC -= a
                minC -= a
                holdsale += a
                ans += a*N
    print(ans)

if __name__ == '__main__':
    main()