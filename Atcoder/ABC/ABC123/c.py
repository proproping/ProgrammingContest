import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import math
    N = int(input())
    trans = [int(input()) for _ in range(5)]
    minind = trans.index(min(trans))
    print(minind+math.ceil(N/min(trans))-1+5-minind)

if __name__ == '__main__':
    main()