import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import itertools
    num = list(map(int,input().split()))
    ans = []
    tmp = list(map(list,itertools.combinations(range(5),3)))
    for i in range(len(tmp)):
        ans.append(num[tmp[i][0]]+num[tmp[i][1]]+num[tmp[i][2]])
    print(sorted(ans)[-3])

if __name__ == '__main__':
    main()