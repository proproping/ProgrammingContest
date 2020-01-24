import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b = map(int,input().split())
    if a <= b:
        print(a)
    else:
        print(a-1)

if __name__ == '__main__':
    main()