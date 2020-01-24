import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    W = list(map(int,input().split()))
    test = list()
    for i in range(N-1):
        test.append(abs(sum(W[0:i+1])-sum(W[i+1:])))
    print(min(test))

if __name__ == '__main__':
    main()