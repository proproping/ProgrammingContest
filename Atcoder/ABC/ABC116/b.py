import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    s = int(input())
    def fn(n):
        if n%2 == 0:
            return n/2
        else:
            return 3*n+1
    tmp = [s]
    flag = 1
    count = 1
    while flag == 1:
        count += 1
        s = fn(s)
        tmp.append(s)
        if s in tmp[:-1]:
            break
    print(count)

if __name__ == '__main__':
    main()