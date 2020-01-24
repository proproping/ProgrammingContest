import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    H,W = map(int,input().split())
    c = [input() for i in range(H)]
    for j in range(H):
        print(c[j])
        print(c[j])

if __name__ == '__main__':
    main()