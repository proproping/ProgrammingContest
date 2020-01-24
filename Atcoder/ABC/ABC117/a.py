import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    T,X = map(int,input().split())
    print(T*1/X)

if __name__ == '__main__':
    main()