import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(M)]

if __name__ == '__main__':
    main()