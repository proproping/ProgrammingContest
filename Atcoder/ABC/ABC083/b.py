import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,A,B = map(int,input().split())
    tmp = []
    for i in range(1,N+1):
        if A <= sum(list(map(int,list(str(i))))) <= B:
            tmp.append(i)
    print(sum(tmp))

if __name__ == '__main__':
    main()