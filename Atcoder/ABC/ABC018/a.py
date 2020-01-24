import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    ans = [0]*3
    tmp1 = [A,B,C]
    tmp2 = sorted([A,B,C],reverse = 1)
    for i in range(3):
        for j in range(3):
            if tmp1[i] == tmp2[j]:
                ans[i] += j+1
    for i in range(3):
        print(ans[i])

if __name__ == '__main__':
    main()