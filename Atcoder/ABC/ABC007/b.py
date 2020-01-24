import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = input()
    if A == "a":
        print(-1)
    else:
        print("a")

if __name__ == '__main__':
    main()