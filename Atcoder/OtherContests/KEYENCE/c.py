import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,K,S = map(int,input().split())
    if S == 10**9:
        ans = [S]*K+[S-1]*(N-K)
        print(*ans,sep = " ")
    else:
        ans = [S]*K+[S+1]*(N-K)
        print(*ans,sep = " ")

if __name__ == '__main__':
    main()