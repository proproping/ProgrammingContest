import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    hh = N//3600
    mm = (N%3600)//60
    ss = (N%3600)%60
    print(str(hh).zfill(2)+":"+str(mm).zfill(2)+":"+str(ss).zfill(2))

if __name__ == '__main__':
    main()