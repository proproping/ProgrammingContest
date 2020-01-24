import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import math
    N = int(input())
    A = list(map(int,input().split()))
    gcd = 10**9
    for i in range(N-1):
        tmp = math.gcd(A[i],A[i+1])
        if tmp < gcd:
            gcd = tmp
    print(gcd)

if __name__ == '__main__':
    main()