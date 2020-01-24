import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    tmp = 2
    while tmp <= N:
        tmp += tmp
    print(int(tmp/2))

if __name__ == '__main__':
    main()