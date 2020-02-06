import numpy as np
def main():
    N = int(input())
    C = list(map(int,input().split()))
    oddC = np.array([C[i] for i in range(N) if i%2 == 0])
    evenC = np.array([C[i] for i in range(N) if i%2 != 0])
    minoddC = min(oddC)
    minC = min(C)
    Q = int(input())
    S = [list(map(int,input().split())) for _ in range(Q)]
    oddlen = len(oddC)
    evenlen = len(evenC)
    ans = 0
    for i in S:
        if i[0] == 1:
            x = i[1]-1
            a = i[2]
            if x%2 != 0:
                if evenC[x//2] >= a:
                    ans += a
                    evenC[x//2] -= a
                    minC = min(minC,evenC[x//2])
                else:
                    continue
            else:
                if oddC[x//2] >= a:
                    ans += a
                    oddC[x//2] -= a
                    minoddC = min(minoddC,oddC[x//2])
                    minC = min(minC,minoddC)
                else:
                    continue

        elif i[0] == 2:
            a = i[1]
            if minoddC >= a:
                ans += a*oddlen
                oddC -= a
                minoddC -= a
                minC = min(minC,minoddC)
            else:
                continue
        else:
            a = i[1]
            if minC >= a:
                ans += a*(oddlen+evenlen)
                evenC -= a
                oddC -= a
                minC -= a
    print(ans)

if __name__ == '__main__':
    main()