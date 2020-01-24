import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,A,B = map(int,input().split())
    print(min([A*N,B]))

if __name__ == '__main__':
    main()