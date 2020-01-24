import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b = map(int,input().split())
    plug = 1
    tap = 0
    while plug < b:
        plug = plug + a - 1
        tap += 1
    print(tap)

if __name__ == '__main__':
    main()