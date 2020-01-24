import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = list(map(int,input().split()))
    flag = 1
    count = 0
    while flag == 1:
        for i in range(N):
            if A[i]%2 != 0:
                flag = 0
                break
            else:
                A[i] = int(A[i]/2)
        count += 1
    print(count-1)

if __name__ == '__main__':
    main()