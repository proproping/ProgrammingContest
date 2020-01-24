import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,i = map(int,input().split())
    print(N-i+1)

if __name__ == '__main__':
    main()