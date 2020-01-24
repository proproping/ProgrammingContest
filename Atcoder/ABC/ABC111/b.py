import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = input()
    if int(N) <= int(N[0]*3):
        print(N[0]*3)
    else:
        print((int(N[0])+1)*111)

if __name__ == '__main__':
    main()