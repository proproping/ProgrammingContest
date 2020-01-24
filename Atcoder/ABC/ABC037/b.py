import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,Q = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(Q)]
    ans = [0]*N
    for i in range(Q):
        for j in range(mat[i][0]-1,mat[i][1]):
            ans[j] = mat[i][2]
    for k in range(len(ans)):
        print(ans[k])

if __name__ == '__main__':
    main()