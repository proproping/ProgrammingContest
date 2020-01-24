import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    r = int(input())
    print(int(r**2))

if __name__ == '__main__':
    main()