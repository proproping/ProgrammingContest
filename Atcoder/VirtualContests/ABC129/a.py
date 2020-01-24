import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    ls = sorted(list(map(int,input().split())))
    print(sum(ls)-max(ls))

if __name__ == '__main__':
    main()