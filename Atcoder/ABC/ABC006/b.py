import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    n = int(input())
    a = 0
    b = 0
    c = 1
    if n >= 4:
        for i in range(3,n):
            tmp = a+b+c
            a = b%10007
            b = c%10007
            c = tmp%10007
        print(c)
    else:
        tmp = [0,0,1]
        print(tmp[n-1])

if __name__ == '__main__':
    main()