import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    ans = 0
    for i in range(min(N,K)+2):
        for j in range(min(N,K)-i):
            print(V[:i])
            print(V[-j-1:])
            if i == 4:
                print("Im fourrrrrrr")

if __name__ == '__main__':
    main()