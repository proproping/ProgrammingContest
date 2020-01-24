import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    print(min([A,B])+min([C,D]))

if __name__ == '__main__':
    main()