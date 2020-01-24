import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    Q = int(input())
    print("ABC") if Q == 1 else print("chokudai")

if __name__ == '__main__':
    main()