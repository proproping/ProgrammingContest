import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import collections
    N,M = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(M)]
    tmp = []
    for i in range(M):
        tmp = tmp + mat[i]
    ans = collections.Counter(tmp)
    for j in range(N):
        print(ans[j+1])

if __name__ == '__main__':
    main()