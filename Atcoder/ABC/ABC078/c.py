import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M = map(int,input().split())
    time = M*1900+(N-M)*100
    p = (1/2)**M
    print(int(time*(1/p)))

if __name__ == '__main__':
    main()