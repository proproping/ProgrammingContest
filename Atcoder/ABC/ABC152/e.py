import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    mod = 10**9+7
    import fractions
    def lcm(a,b):
        return (a*b)//fractions.gcd(a,b)
    N = int(input())
    A = list(map(int,input().split()))
    lc = 1
    for i in range(N):
        lc = lcm(lc,A[i])
    ans = 0
    for i in range(N):
        ans += lc//A[i]
    print(ans%mod)

if __name__ == '__main__':
    main()