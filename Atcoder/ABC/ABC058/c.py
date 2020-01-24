import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import collections
    n = int(input())
    S = [input() for _ in range(n)]
    abc = list("abcdefghijklmnopqrstuvwxyz")
    dic = dict(zip(abc,[10**9]*len(abc)))
    for i in range(n):
        tmp = collections.Counter(list(S[i]))
        for j in abc:
            if dic[j] > tmp[j]:
                dic[j] = tmp[j]
    ans = []
    for k in abc:
        for l in range(dic[k]):
            ans.append(k)
    print(*ans,sep="")

if __name__ == '__main__':
    main()