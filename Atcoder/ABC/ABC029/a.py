import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    W = input()
    print(W+"s")

if __name__ == '__main__':
    main()