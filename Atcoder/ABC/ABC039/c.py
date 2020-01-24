import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    ans = "WWBWBWW"
    tmp = 0
    for i in range(13):
        if S[i:i+7] == ans:
            tmp = i
            break
    ansdic = {0:"Si",1:"La",2:"La",3:"So",4:"So",5:"Fa",6:"Fa",7:"Mi",8:"Re",9:"Re",10:"Do",11:"Do"}
    print(ansdic[tmp])

if __name__ == '__main__':
    main()