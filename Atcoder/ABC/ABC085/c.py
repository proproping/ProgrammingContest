import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,Y = map(int,input().split())
    A,B,C = -1,-1,-1
    flag = False
    for i in range(N+1):
        if flag:
            break
        for j in range(N+1-i):
            if i*10000 + j*5000 + (N-i-j)*1000 == Y and (N-i-j) >= 0:
                A,B,C = i,j,(N-i-j)
                flag = True
                break
    print(A,B,C)

if __name__ == '__main__':
    main()