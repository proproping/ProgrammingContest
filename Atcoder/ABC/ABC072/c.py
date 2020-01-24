import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    a = list(map(int,input().split()))
    num = list(range(10**5+1))
    val = [0]*(10**5+1)
    dic = dict(zip(num,val))
    for i in a:
        if i == 0:
            dic[i] += 1
            dic[i+1] += 1
        elif i == 10**5:
            dic[i-1] += 1
            dic[i] += 1
        else:
            dic[i-1] += 1
            dic[i] += 1
            dic[i+1] += 1
    print(max(dic.values()))

if __name__ == '__main__':
    main()