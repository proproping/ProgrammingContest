import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,K = map(int,input().split())
    if K > (N-1)*(N-2)//2:
        print(-1)
    M = (N-1) + ((N-1)*(N-2)//2-K)
    tree = [[1,i] for i in range(2,N+1)]
    for i in range(2,(M-(N-1)//2-K)+3):
        tree.append([i,i+1])
    print(M)
    for i in range(len(tree)):
        print(*tree[i],sep = " ")

if __name__ == '__main__':
    main()