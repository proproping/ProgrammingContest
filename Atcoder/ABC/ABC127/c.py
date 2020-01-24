import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(M)]
    L = 0
    R = 10**5+1
    for i in range(M):
        if L < mat[i][0]:
            L = mat[i][0]
        if R > mat[i][1]:
            R = mat[i][1]
    print(max([R-L+1,0]))

if __name__ == '__main__':
    main()