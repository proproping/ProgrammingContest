import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,K = map(int,input().split())
    if N == 1:
        print(K)
    else:
        print(K*(K-1)**(N-1))

if __name__ == '__main__':
    main()