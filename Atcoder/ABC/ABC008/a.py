import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S,T = map(int,input().split())
    print(T-S+1)

if __name__ == '__main__':
    main()