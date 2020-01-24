import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X = int(input())
    tmp = X//100
    lis = list(range(tmp*100,tmp*100+5*tmp+1))
    if X in lis:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()