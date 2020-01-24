import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,M = map(int,input().split())
    A = [input() for i in range(N)]
    B = [input() for j in range(M)]
    W = len(list(A[0]))-len(list(B[0]))+1
    H = N - M + 1
    ans = "No"
    for i in range(H):
        for j in range(W):
            tmpA = []
            for k in range(M):
                 tmpA.append(A[i+k][j:j+len(list(B[0]))])
            if tmpA == B:
                ans = "Yes"
                break
    print(ans)

if __name__ == '__main__':
    main()