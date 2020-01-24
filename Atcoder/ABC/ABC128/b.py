import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    tmp = list()
    for i in range(N):
        s,p = input().split()
        tmp.append([s,int(p),i+1])
    tmp = sorted(tmp, key = lambda x:x[1], reverse = 1)
    tmp = sorted(tmp, key = lambda x:x[0])
    tmp = [x[2] for x in tmp]
    for i in range(N):
        print(tmp[i])

if __name__ == '__main__':
    main()