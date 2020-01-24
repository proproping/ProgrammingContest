import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from math import ceil
    N = int(input())
    print(ceil(N/2)-1)

if __name__ == '__main__':
    main()