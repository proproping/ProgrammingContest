import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    w = list(input())
    tmp1 = sorted(list(set(w)))
    flag = 1
    for i in range(len(tmp1)):
        count = 0
        for j in range(len(w)):
            if w[j] == tmp1[i]:
                count += 1
        if count%2 != 0:
            flag = 0
            break
    if flag == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()