import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    c = input()
    if c in ["a","e","i","o","u"]:
        print("vowel")
    else:
        print("consonant")

if __name__ == '__main__':
    main()