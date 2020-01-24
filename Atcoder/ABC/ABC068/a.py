import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    print("ABC"+str(N))

if __name__ == '__main__':
    main()