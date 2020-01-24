import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = input()
    if "9" in N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()