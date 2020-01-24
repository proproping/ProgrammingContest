import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    tmp1 = N//2
    tmp2 = N%2
    ans = [2]*tmp1
    if tmp2 != 0:
        ans.append(1)
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()