import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a,b = map(int,input().split())
    tmp = []
    tmp.append(str(a)*b)
    tmp.append(str(b)*a)
    tmp = sorted(tmp)
    print(tmp[0])

if __name__ == '__main__':
    main()