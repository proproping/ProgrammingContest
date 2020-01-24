import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    S = [input() for i in range(N)]
    tmp1 = list(set(S))
    dic = {}
    for i in range(len(tmp1)):
        dic.setdefault(tmp1[i],i)
    tmp2 = [0]*len(tmp1)
    for i in S:
        tmp2[dic[i]] += 1
    print(tmp1[tmp2.index(max(tmp2))])

if __name__ == '__main__':
    main()