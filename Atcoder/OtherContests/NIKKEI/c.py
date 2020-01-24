import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    ans = "YES"
    for i in range(N):
        if A[i] > B[i]:
            ans = "NO"
            break
    print(ans)

if __name__ == '__main__':
    main()