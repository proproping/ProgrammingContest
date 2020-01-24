import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M = map(int,input().split())
    if N == M:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()