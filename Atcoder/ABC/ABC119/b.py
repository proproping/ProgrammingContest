import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    matrix = [input().split() for i in range(N)]
    ans = 0
    for i in range(N):
        if matrix[i][1] == "JPY":
            ans += float(matrix[i][0])
        else:
            ans += float(matrix[i][0])*float(380000.0)
    print(ans)

if __name__ == '__main__':
    main()