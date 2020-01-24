import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,S,T = map(int,input().split())
    W = int(input())
    A = [int(input()) for i in range(N-1)]
    ans = 0
    if S <= W <= T:
        ans += 1
    for i in range(len(A)):
        W += A[i]
        if S <= W <= T:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()