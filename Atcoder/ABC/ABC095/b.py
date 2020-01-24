import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,X = map(int,input().split())
    m = [int(input()) for i in range(N)]
    ans = len(m)
    f = X - sum(m)
    ans += f//min(m)
    print(ans)

if __name__ == '__main__':
    main()