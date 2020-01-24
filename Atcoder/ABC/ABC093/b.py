import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,K = map(int,input().split())
    if A == B:
        print(A)
    if K > B - A:
        K = B - A
    tmp1 = list(range(A,A+K))
    tmp2 = list(range(B-K+1,B+1))
    ans = sorted(list(set(tmp1 + tmp2)))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()