import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    a = [[i,int(tmp)] for i, tmp in enumerate(input().split(),1)]
    a.sort(key = lambda x:x[1], reverse=True)
    for i in range(N):
        print(a[i][0])

if __name__ == '__main__':
    main()