import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    p = []
    N = int(input())
    for i in range(N):
        p.append(int(input()))
    ans = sum(p)-(max(p)/2)
    print(int(ans))

if __name__ == '__main__':
    main()