import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    ls = sorted(list(map(int,input().split())))
    x = ls[2]*2 - ls[0] - ls[1]
    if x%2 == 1:
        x += 3
    print(x//2)

if __name__ == '__main__':
    main()