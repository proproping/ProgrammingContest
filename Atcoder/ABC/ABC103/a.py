import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = list(map(int,input().split()))
    print(max(A)-min(A))

if __name__ == '__main__':
    main()