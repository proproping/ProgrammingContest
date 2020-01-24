import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A1 = list(map(int,input().split()))
    A2 = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        tmp = 0
        tmp = sum(A1[:i+1])+sum(A2[i:])
        if tmp > ans:
            ans = tmp
    print(ans)

if __name__ == '__main__':
    main()