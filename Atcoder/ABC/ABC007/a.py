import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    n = int(input())
    print(n-1)

if __name__ == '__main__':
    main()