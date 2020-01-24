import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from operator import itemgetter
    N = int(input())
    ls = []
    for i in range(N):
        s,p = input().split()
        p = int(p)
        ls.append([s,p,i+1])
    ls = sorted(ls,key=itemgetter(1),reverse=True)
    ls = sorted(ls,key=itemgetter(0))
    for i in range(len(ls)):
        print(ls[i][2])

if __name__ == '__main__':
    main()