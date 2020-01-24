import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a = int(input())
    b = int(input())
    if a%b == 0:
        print(0)
    else:
        print(b-(a%b))

if __name__ == '__main__':
    main()