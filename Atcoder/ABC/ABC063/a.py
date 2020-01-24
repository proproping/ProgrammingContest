import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    if A+B >= 10:
        print("error")
    else:
        print(A+B)

if __name__ == '__main__':
    main()