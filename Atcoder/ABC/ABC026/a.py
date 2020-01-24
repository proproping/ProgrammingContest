import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = int(input())
    print((A/2)**2)

if __name__ == '__main__':
    main()