import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    mat = [list(map(int,input().split())) for i in range(N-1)]
    dic = dict(zip(range(1,N+1),[0]*N))
    for i in range(N-1):
        for j in range(2):
            dic[mat[i][j]] += 1
    K = max(dic.values())
    index = max(dic.items(),key = lambda x:x[1])[0]
    save = [[] for i in range(N)]
    tmp = [0]*(N-1)
    num = 1
    for i in range(N-1):
        if index in mat[i]:
            tmp[i] = num
            save[mat[i][0]-1].append(num)
            save[mat[i][1]-1].append(num)
            num += 1
    if 0 not in tmp:
        print(K)
        for i in range(len(tmp)):
            print(tmp[i])
    else:
        for i in range(len(tmp)):
            if tmp[i] == 0:
                for j in range(1,K+1):
                    if j not in save[mat[i][0]-1] and j not in save[mat[i][1]-1]:
                        tmp[i] = j
                        save[mat[i][0]-1].append(j)
                        save[mat[i][1]-1].append(j)
        print(K)
        for k in range(len(tmp)):
            print(tmp[i])

if __name__ == '__main__':
    main()