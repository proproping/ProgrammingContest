import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    S = list(input())
    al = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dic1 = dict(zip(al,list(range(len(al)))))
    tmp = []
    for i in S:
        tmp.append((dic1[i]+N)%26)
    dic2 = dict(zip(list(range(len(al))),al))
    ans = []
    for j in tmp:
        ans.append(dic2[j])
    print(*ans,sep="")

if __name__ == '__main__':
    main()