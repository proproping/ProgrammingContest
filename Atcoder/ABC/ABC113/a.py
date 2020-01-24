import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X,Y = map(int,input().split())
    print(int(X+(Y/2)))

if __name__ == '__main__':
    main()