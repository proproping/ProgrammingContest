import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b = map(int,input().split())
    gap = b - a
    btall = sum(list(range(1,gap+1)))
    print(btall - b)

if __name__ == '__main__':
    main()