import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    H,W = map(int,input().split())
    S = [list(input()) for i in range(H)]
    S.insert(0,[0]*W)
    S.append([0]*W)
    for i in range(len(S)):
        S[i].insert(0,0)
        S[i].append(0)
    dx = [1,0,-1,0,1,-1,-1,1]
    dy = [0,1,0,-1,1,1,-1,-1]
    tmp = [[0] * W for i in range(H)]
    for i in range(1,H+1):
        for j in range(1,W+1):
            if S[i][j] == "#":
                tmp[i-1][j-1] = "#"
                continue
            num = 0
            for k in range(len(dx)):
                if S[i+dx[k]][j+dy[k]] == "#":
                    num += 1
                    tmp[i-1][j-1] = num
    for j in range(len(tmp)):
        print(*tmp[j],sep = "")

if __name__ == '__main__':
    main()