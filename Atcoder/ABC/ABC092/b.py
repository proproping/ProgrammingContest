import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    D,X = map(int,input().split())
    A = [int(input()) for i in range(N)]
    count = N
    for i in range(N):
        tmp = A[i]
        while (A[i]+1) <= D:
            count += 1
            A[i] += tmp
    print(count+X)

if __name__ == '__main__':
    main()