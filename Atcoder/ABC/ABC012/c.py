import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    tmp = 2025 - N
    ans = []
    for i in range(1,10):
        if tmp%i == 0 and tmp//i < 10:
            ans.append([i,tmp//i])
    for i in range(len(ans)):
        print(*ans[i],sep=" x ")

if __name__ == '__main__':
    main()