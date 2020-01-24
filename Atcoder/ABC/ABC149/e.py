import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())),reverse=1)
    ans = 0
    if M >= (N**2//2):
        ans = sum(A)*2*N
        for i in range((N**2-M)):
            ans -= 0
    else:
        for i in range(M):
            ans += 0
    print(ans)

if __name__ == '__main__':
    main()