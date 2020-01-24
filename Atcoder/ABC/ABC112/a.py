import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    if N == 1:
        print("Hello World")
    else:
        A = int(input())
        B = int(input())
        print(A+B)

if __name__ == '__main__':
    main()