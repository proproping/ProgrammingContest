import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X,Y = map(int,input().split())
    print(max(X,Y))

if __name__ == '__main__':
    main()