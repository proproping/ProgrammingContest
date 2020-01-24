import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = int(input())
    print(N**2-A)

if __name__ == '__main__':
    main()