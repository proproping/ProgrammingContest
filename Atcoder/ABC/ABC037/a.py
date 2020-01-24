import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C = map(int,input().split())
    ans = 0
    ans += (C//min([A,B]))
    ans += ((C-ans*min([A,B]))//max([A,B]))
    print(ans)

if __name__ == '__main__':
    main()