import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())
    if N <= K:
        print(X*N)
    else:
        print(X*K+Y*(N-K))

if __name__ == '__main__':
    main()