import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M,X,Y = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    ans = "War"
    for i in range(X+1,Y):
        if max(x) < i and min(y) >= i:
            ans = "No War"
            break
    print(ans)

if __name__ == '__main__':
    main()