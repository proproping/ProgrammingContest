import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X,Y = map(str,input().split())
    if X == Y:
        print("=")
    elif X < Y:
        print("<")
    else:
        print(">")

if __name__ == '__main__':
    main()