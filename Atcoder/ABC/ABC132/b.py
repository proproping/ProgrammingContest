import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(n-2):
        if p[i] < p[i+1] < p[i+2] or p[i] > p[i+1] > p[i+2]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()