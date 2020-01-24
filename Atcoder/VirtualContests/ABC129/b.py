import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    W = list(map(int,input().split()))
    tmp = []
    for i in range(N-1):
        tmp.append(abs(sum(W[:i+1])-sum(W[i+1:])))
    print(min(tmp))

if __name__ == '__main__':
    main()