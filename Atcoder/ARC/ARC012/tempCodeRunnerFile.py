import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    day = str(input())
    dic = dict(zip(["Monday","Tuesday","Wendesday","Thursday","Friday","Saturday","Sunday"],[5,4,3,2,1,0,0]))
    print(dic[day])

if __name__ == '__main__':
    main()