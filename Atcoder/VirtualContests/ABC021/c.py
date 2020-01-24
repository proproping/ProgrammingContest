import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import numpy as np
    from scipy.sparse.csgraph import shortest_path
    N = int(input())
    a,b = map(int,input().split())
    M = int(input())
    matrix = [np.array([0]*N) for i in range(N)]
    for i in range(M):
        r,c = map(int,input().split())
        matrix[r-1][c-1] = 1
        matrix[c-1][r-1] = 1
    matrix = np.array(matrix)
    dis = shortest_path(matrix)[a-1]
    dis = list(map(int,list(dis)))
    gooddis = dis[b-1]
    dis = sorted(dis)
    ind = dis.index(gooddis)
    dis = dis[1:ind]
    num = range(1,dis[-1]+1)
    count = [0]*len(num)
    dic = dict(zip(num,count))
    for i in dis:
        dic[i] += 1
    ans = 1
    for j in list(dic.values()):
        ans *= j
    print(ans)

if __name__ == '__main__':
    main()