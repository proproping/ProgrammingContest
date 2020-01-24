import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a = int(input())
    b = int(input())
    h = int(input())
    print(int((a+b)*h/2))

if __name__ == '__main__':
    main()