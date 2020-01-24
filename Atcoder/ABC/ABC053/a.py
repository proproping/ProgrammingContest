import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    x = int(input())
    print("ABC") if x < 1200 else print("ARC")

if __name__ == '__main__':
    main()