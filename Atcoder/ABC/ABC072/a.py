import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X,t = map(int,input().split())
    if X < t:
        print(0)
    else:
        print(X-t)

if __name__ == '__main__':
    main()