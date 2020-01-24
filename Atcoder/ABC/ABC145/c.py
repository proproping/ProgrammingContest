import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import itertools
    N = int(input())
    xy = [list(map(int,input().split())) for i in range(N)]
    tmp = list(itertools.permutations(list(range(N)),N))
    length = []
    for i in range(len(tmp)):
        tmplen = 0
        for j in range(N-1):
            tmplen += ((xy[tmp[i][j]][0]-xy[tmp[i][j+1]][0])**2+(xy[tmp[i][j]][1]-xy[tmp[i][j+1]][1])**2)**(1/2)
        length.append(tmplen)
    print(sum(length)/len(length))

if __name__ == '__main__':
    main()