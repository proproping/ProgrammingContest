import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X,Y,Z = map(int,input().split())
    count = 0
    X += -Z
    while X >= (Y+Z):
        X += -(Y+Z)
        count += 1
    print(count)

if __name__ == '__main__':
    main()