import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M,A,B = map(int,input().split())
    c = [int(input()) for _ in range(M)]
    for i in range(M):
        if N <= A:
            N += B
        N -= c[i]
        if N < 0:
            print(i+1)
            break
        if i == M-1:
            print("complete")

if __name__ == '__main__':
    main()