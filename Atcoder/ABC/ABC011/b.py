import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    print(str.capitalize(S))

if __name__ == '__main__':
    main()