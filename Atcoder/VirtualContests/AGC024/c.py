import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

if __name__ == '__main__':
    main()