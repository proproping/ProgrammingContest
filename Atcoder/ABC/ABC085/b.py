import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    d = set([int(input()) for i in range(N)])
    print(len(d))

if __name__ == '__main__':
    main()