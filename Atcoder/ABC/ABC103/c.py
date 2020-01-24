import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    a = list(map(int,input().split()))
    print(sum(a)-N)

if __name__ == '__main__':
    main()