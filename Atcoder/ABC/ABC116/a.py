import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    AB,BC,CA = map(int,input().split())
    print(int(AB*BC/2))

if __name__ == '__main__':
    main()