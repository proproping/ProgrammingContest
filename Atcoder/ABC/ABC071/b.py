import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    tmp = list("abcdefghijklmnopqrstuvwxyz")
    ans = []
    for i in range(len(tmp)):
        if tmp[i] not in S:
            ans.append(tmp[i])
    if len(ans) == 0:
        print("None")
    else:
        print(ans[0])

if __name__ == '__main__':
    main()