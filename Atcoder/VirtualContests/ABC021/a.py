import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    print(N)
    for i in range(N):
        print(1)

if __name__ == '__main__':
    main()