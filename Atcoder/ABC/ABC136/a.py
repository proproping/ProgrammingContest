import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b,c = map(int, input().split())
    if (c-(a-b)) <= 0:
        print(0)
    else:
        print(c-(a-b))

if __name__ == '__main__':
    main()