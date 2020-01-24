import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    K,X = map(int,input().split())
    if 500*K >= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()