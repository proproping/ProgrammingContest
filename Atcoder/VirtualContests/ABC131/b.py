import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,L = map(int,input().split())
    t = [L+i-1 for i in range(1,N+1)]
    abst = list(map(abs,t))
    minind = abst.index(min(abst))
    print(sum(t)-t[minind])

if __name__ == '__main__':
    main()