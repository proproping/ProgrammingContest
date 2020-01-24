import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    print(len(A)-len(list(set(A))))

if __name__ == '__main__':
    main()