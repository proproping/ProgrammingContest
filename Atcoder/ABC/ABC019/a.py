import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from statistics import median
    a,b,c = map(int,input().split())
    print(median([a,b,c]))

if __name__ == '__main__':
    main()