import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    x,a,b = map(int,input().split())
    if abs(x-a) > abs(x-b):
        print("B")
    else:
        print("A")

if __name__ == '__main__':
    main()