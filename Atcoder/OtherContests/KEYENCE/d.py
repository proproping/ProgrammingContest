import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    flag = False
    ans = 0
    count = 0
    while True:
        if count == 10**5:
            ans = -1
            break
        for i in range(1,N):
            if A[i-1] > A[i]:
                break
            if i == N-1:
                flag = True
        if flag:
            break
        for i in range(1,N):
            if B[i-1] > B[i] or A[i-1] > A[i]:
                tmpA = [A[i-1],A[i]]
                tmpB = [B[i-1],B[i]]
                A[i-1],A[i] = tmpB[1],tmpB[0]
                B[i-1],B[i] = tmpA[1],tmpA[0]
                ans += 1
        count += 1
    print(ans)

if __name__ == '__main__':
    main()