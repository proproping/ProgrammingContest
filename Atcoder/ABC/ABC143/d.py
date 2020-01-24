import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import itertools
    import bisect
    N = int(input())
    L = sorted(list(map(int,input().split())))
    ans = 0
    for i in range(N-2):
        a = L[i]
        for j in range(i+1,N-1):
            b = L[j]
            ind_cmin = j+1
            ind_cmax = bisect.bisect_left(L,a+b)-1
            ans += ind_cmax - ind_cmin + 1
    print(ans)

if __name__ == '__main__':
    main()