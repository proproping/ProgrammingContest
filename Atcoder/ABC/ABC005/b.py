import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    T = [int(input()) for i in range(N)]
    print(min(T))

if __name__ == '__main__':
    main()