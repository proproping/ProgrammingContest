import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    R = int(input())
    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")

if __name__ == '__main__':
    main()