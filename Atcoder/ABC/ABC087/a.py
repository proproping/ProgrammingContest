import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X = int(input())
    A = int(input())
    B = int(input())
    print((X-A)%B)

if __name__ == '__main__':
    main()