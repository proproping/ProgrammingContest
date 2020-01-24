import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    c = [list(map(int,input().split())) for _ in range(3)]
    a = [0]*3
    b = c[0]
    a[1] = c[1][0]-b[0]
    a[2] = c[2][0]-b[0]
    flag = False
    ans = "Yes"
    for i in range(3):
        if flag:
            break
        for j in range(3):
            if c[i][j] != a[i]+b[j]:
                ans = "No"
                flag = True
                break
    print(ans)

if __name__ == '__main__':
    main()