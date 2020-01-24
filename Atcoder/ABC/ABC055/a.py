import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    x = 800*N
    y = 200*(N//15)
    print(x-y)

if __name__ == '__main__':
    main()