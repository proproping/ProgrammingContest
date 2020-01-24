import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from math import ceil
    a,b = map(int,input().split())
    print(ceil((a+b)/2))

if __name__ == '__main__':
    main()