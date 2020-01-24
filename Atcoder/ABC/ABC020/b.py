import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = input().split()
    print(int(A+B)*2)

if __name__ == '__main__':
    main()