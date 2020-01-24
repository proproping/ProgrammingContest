import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,P = map(int,input().split())
    print((A*3+P)//2)

if __name__ == '__main__':
    main()