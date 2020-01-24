import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X = input()
    dic = {"A":1,"B":2,"C":3,"D":4,"E":5}
    print(dic[X])

if __name__ == '__main__':
    main()