import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C = map(int,input().split())
    print(A*B*C%(10**9+7))

if __name__ == '__main__':
    main()