import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    print((N+1)//2)

if __name__ == '__main__':
    main()