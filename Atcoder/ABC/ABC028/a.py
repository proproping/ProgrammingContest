import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    if N == 100:
        print("Perfect")
    elif 99 >= N >= 90:
        print("Great")
    elif 89 >= N >= 60:
        print("Good")
    else:
        print("Bad")

if __name__ == '__main__':
    main()