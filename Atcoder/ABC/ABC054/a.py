import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A,B = map(int,input().split())
    tmp = [A,B]
    ans = ["Alice","Bob"]
    if tmp[0] == tmp[1]:
        print("Draw")
    elif tmp[0] == 1:
        print(ans[0])
    elif tmp[1] == 1:
        print(ans[1])
    elif tmp[0] > tmp[1]:
        print(ans[0])
    else:
        print(ans[1])

if __name__ == '__main__':
    main()