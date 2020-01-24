import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    C = input()
    ls = list("abcdefghijklmnopqrstuvwxyz")
    num = list(range(0,26))
    dic = dict(zip(ls,num))
    print(ls[dic[C]+1])

if __name__ == '__main__':
    main()