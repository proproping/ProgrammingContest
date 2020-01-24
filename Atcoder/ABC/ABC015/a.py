import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = input()
    B = input()
    print(A) if len(A) > len(B) else print(B)

if __name__ == '__main__':
    main()