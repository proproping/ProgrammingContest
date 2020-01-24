import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    a = str(input())
    if a == "Sunny":
        print("Cloudy")
    elif a == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")

if __name__ == '__main__':
    main()