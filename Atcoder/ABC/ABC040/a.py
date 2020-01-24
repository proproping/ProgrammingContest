import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    n,x = map(int,input().split())
    print(x-1) if (x-1) < (n-x) else print(n-x)

if __name__ == '__main__':
    main()