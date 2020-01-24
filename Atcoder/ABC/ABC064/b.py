import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    a = list(map(int,input().split()))
    print(max(a)-min(a))

if __name__ == '__main__':
    main()