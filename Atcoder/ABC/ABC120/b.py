import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,K = map(int,input().split())
    tmp = []
    for i in range(100):
        if A%(i+1) == 0:
            if B%(i+1) == 0:
                tmp.append(i+1)
    print(tmp[len(tmp)-K])

if __name__ == '__main__':
    main()