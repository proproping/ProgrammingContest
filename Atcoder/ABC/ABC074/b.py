import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    K = int(input())
    x = list(map(int,input().split()))
    count = 0
    for i in range(len(x)):
        count += min([x[i]*2,abs(x[i]-K)*2])
    print(count)

if __name__ == '__main__':
    main()