import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from math import floor
    x,y = map(int,input().split())
    print(floor(y/x))

if __name__ == '__main__':
    main()