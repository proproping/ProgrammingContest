import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    print(max([A+B,A-B,A*B]))

if __name__ == '__main__':
    main()