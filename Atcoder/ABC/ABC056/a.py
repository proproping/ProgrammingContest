import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b = map(str,input().split())
    if a == b:
        print("H")
    else:
        print("D")

if __name__ == '__main__':
    main()