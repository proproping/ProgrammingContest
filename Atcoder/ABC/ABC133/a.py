import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    n,a,b = map(int, input().split())
    print(min(a*n,b))

if __name__ == '__main__':
    main()