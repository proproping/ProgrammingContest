import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    from math import ceil
    tmp1 = [A,B,C,D,E]
    tmp2 = list()
    for j in range(5):
        if tmp1[j]%10 == 0:
            tmp2.append(0)
        else:
            tmp2.append(10 - tmp1[j]%10)
    for i in range(5):
        tmp1[i] = ceil(tmp1[i]/10)*10
    print(sum(tmp1)-max(tmp2))

if __name__ == '__main__':
    main()