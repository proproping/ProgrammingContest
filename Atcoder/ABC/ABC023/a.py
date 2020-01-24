import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X = int(input())
    print((X//10)+(X%10))

if __name__ == '__main__':
    main()