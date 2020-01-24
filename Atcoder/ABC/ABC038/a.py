import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    print("YES") if S[-1] == "T" else print("NO")

if __name__ == '__main__':
    main()