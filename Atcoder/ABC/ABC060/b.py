import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B,C = map(int,input().split())
    tmpA = A
    tmp = []
    while A%B != C and A%B not in tmp:
        tmp.append(A%B)
        A += tmpA
    if A%B == C:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()