import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    SA = list(input())
    SB = list(input())
    SC = list(input())
    gameflag = 1
    flag = "a"
    while gameflag == 1:
        if flag == "a":
            if SA == []:
                break
            else:
                flag = SA.pop(0)
        if flag == "b":
            if SB == []:
                break
            else:
                flag = SB.pop(0)
        if flag == "c":
            if SC == []:
                break
            else:
                flag = SC.pop(0)
    print(str.upper(flag))

if __name__ == '__main__':
    main()