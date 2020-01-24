import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    R = int(input())
    G = int(input())
    print(G*2-R)

if __name__ == '__main__':
    main()