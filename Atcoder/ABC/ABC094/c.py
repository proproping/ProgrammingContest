import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    X = list(map(int,input().split()))
    Y = sorted(X)
    index = N//2
    a,b = Y[index],Y[index-1]
    for i in range(N):
        if X[i] < a:
            print(a)
        else:
            print(b)

if __name__ == '__main__':
    main()