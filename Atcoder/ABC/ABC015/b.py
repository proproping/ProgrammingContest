import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from math import ceil
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if A[i] == 0:
            count += 1
    print(ceil(sum(A)/(N-count)))

if __name__ == '__main__':
    main()