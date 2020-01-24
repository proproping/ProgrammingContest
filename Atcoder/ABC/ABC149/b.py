import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,K = map(int,input().split())
    if K <= A:
        print(A-K,B)
    else:
        print(0,max(0,B-(K-A)))

if __name__ == '__main__':
    main()