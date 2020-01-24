import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b,x = map(int,input().split())
    tmp1 = b//x
    tmp2 = (a-1)//x
    print(tmp1-tmp2)

if __name__ == '__main__':
    main()