import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    dic = {"SAT":1,"FRI":2,"THU":3,"WED":4,"TUE":5,"MON":6,"SUN":7}
    print(dic[S])

if __name__ == '__main__':
    main()