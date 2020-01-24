import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    L,H = map(int,input().split())
    N = int(input())
    A = [int(input()) for i in range(N)]
    ans = []
    for i in range(len(A)):
        if A[i] < L:
            ans.append(L - A[i])
        elif A[i] > H:
            ans.append(-1)
        else:
            ans.append(0)
    for j in range(len(ans)):
        print(ans[j])

if __name__ == '__main__':
    main()