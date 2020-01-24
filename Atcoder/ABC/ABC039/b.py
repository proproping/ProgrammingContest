import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X = int(input())
    print(int(X**(1/4)))

if __name__ == '__main__':
    main()