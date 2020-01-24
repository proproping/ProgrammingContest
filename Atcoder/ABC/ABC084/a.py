import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    M = int(input())
    print(48-M)

if __name__ == '__main__':
    main()