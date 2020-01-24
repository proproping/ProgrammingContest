import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = int(input())
    if N%500 > A:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()