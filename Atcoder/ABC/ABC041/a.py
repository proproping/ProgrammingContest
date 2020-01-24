import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    s = input()
    i = int(input())
    print(s[i-1])

if __name__ == '__main__':
    main()