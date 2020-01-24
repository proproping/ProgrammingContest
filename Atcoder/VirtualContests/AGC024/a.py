import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C,K = map(int,input().split())
    if abs(A-B) > 10**18:
        print("Unfair")
    else:
        print((A-B)*(-1)**(K))

if __name__ == '__main__':
    main()