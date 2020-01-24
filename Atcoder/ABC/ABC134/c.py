import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    maxind = A.index(max(A))
    maxa = max(A)
    A = sorted(A)
    ans = [maxa]*maxind
    ans.append(A[-2])
    [ans.append(i) for i in [maxa]*(N-maxind-1)]
    print(*ans,sep="\n")

if __name__ == '__main__':
    main()