import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,L = map(int,input().split())
    S = [input() for i in range(N)]
    print("".join(sorted(S)))

if __name__ == '__main__':
    main()