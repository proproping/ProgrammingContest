import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    if A > 8 or B > 8:
        print(":(")
    else:
        print("Yay!")

if __name__ == '__main__':
    main()