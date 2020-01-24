import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a = int(input())
    b = int(input())
    n = int(input())
    while n%a != 0 or n%b != 0:
        n += 1
    print(n)

if __name__ == '__main__':
    main()