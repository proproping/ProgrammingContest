import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    L = [2,1]
    if N > 1:
        for i in range(2,N+1):
            L.append(L[i-1]+L[i-2])
    print(L[N])

if __name__ == '__main__':
    main()