import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    print(str(B)+" "+str(A))

if __name__ == '__main__':
    main()