import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = input()
    print("SAME") if N[0]*4 == N else print("DIFFERENT")

if __name__ == '__main__':
    main()