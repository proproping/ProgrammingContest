import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C,D = map(int,input().split())
    if (A+B) - (C+D) == 0:
        print("Balanced")
    elif (A+B) - (C+D) > 0:
        print("Left")
    else:
        print("Right")

if __name__ == '__main__':
    main()