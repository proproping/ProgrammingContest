import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import math
    H = int(input())
    W = int(input())
    N = int(input())
    which = max(H,W)
    print(math.ceil(N/which))

if __name__ == '__main__':
    main()