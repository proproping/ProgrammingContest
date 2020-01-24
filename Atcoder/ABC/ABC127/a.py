import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    ans = B
    if A >= 13:
        print(ans)
    elif 6 <= A <= 12:
        print(int(ans/2))
    else:
        print(0)

if __name__ == '__main__':
    main()