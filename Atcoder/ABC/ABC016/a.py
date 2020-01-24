import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    M,D = map(int,input().split())
    print("YES") if M%D == 0 else print("NO")

if __name__ == '__main__':
    main()