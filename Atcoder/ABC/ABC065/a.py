import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X,A,B = map(int,input().split())
    if X < abs(A-B):
        print("dangerous")
    elif A-B >= 0:
        print("delicious")
    else:
        print("safe")

if __name__ == '__main__':
    main()