import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = list(map(str,input().split(",")))
    tmp = " ".join(S)
    print(tmp)

if __name__ == '__main__':
    main()