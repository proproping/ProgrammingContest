import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M = map(int,input().split())
    count = 0
    if N <= M//2:
        count += N
        M -= N*2
    else:
        count += M//2
        M = 0
    count += M//4
    print(count)

if __name__ == '__main__':
    main()