import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    mat = [list(map(int,input().split())) for i in range(3)]
    ans = 0
    for i in range(3):
        ans += mat[i][0] * mat[i][1] / 10
    print(int(ans))

if __name__ == '__main__':
    main()