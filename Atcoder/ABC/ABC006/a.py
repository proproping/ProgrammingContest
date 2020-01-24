import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    if N%3 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()