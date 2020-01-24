import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    n,m = map(int,input().split())
    print((n-1)*(m-1))

if __name__ == '__main__':
    main()