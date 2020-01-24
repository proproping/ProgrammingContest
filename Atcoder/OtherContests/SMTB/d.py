import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    S = list(input())
    pas = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                pas.append(str(i)+str(j)+str(k))
    ans = 0
    for pw in pas:
        if pw[0] in S:
            ind = S.index(pw[0])
            tmp = S[ind+1:]
        else:
            continue
        if pw[1] in tmp:
            ind = tmp.index(pw[1])
            tmp = tmp[ind+1:]
        else:
            continue
        if pw[2] in tmp:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()