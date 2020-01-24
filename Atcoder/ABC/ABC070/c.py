import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from fractions import gcd
    N = int(input())
    T = list(set([int(input()) for _ in range(N)]))
    ans = 1
    def lcm(a,b):
        return (a*b)//gcd(a,b)
    for i in range(len(T)):
        ans = lcm(ans,T[i])
    print(ans)

if __name__ == '__main__':
    main()