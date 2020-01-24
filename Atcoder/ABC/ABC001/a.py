import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    H1 = int(input())
    H2 = int(input())
    print(H1-H2)

if __name__ == '__main__':
    main()