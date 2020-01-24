import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = list(input())
    tmp = 0
    for i in range(len(N)):
        tmp += int(N[i])
    if int("".join(N))%tmp == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()