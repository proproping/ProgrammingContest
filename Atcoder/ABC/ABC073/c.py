import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    keys = list(set(A))
    values = [0]*len(keys)
    dic = {}
    dic.update(zip(keys,values))
    for i in A:
        dic[i] += 1
    tmp = [i%2 for i in dic.values()]
    print(sum(tmp))

if __name__ == '__main__':
    main()