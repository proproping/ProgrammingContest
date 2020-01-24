import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    if N <= 999:
        print("ABC")
    else:
        print("ABD")

if __name__ == '__main__':
    main()