import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    x,y = map(int,input().split())
    print("Better") if y > x else print("Worse")

if __name__ == '__main__':
    main()