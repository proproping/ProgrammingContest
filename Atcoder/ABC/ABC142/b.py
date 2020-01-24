import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()