import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C = map(int,input().split())
    tmp = sorted([A,B,C])
    if tmp[0] == tmp[1]:
        print(tmp[2])
    else:
        print(tmp[0])

if __name__ == '__main__':
    main()