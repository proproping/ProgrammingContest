import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = int(input())
    B = int(input())
    if A == B:
        print("EQUAL")
    elif A < B:
        print("LESS")
    else:
        print("GREATER")

if __name__ == '__main__':
    main()