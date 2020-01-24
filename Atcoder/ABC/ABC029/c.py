import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    dic = {0:"a",1:"b",2:"c"}
    for a in range(3):
        for b in range(3):
            if N == 1:
                print(dic[a])
                break
            for c in range(3):
                if N == 2:
                    print(dic[a]+dic[b])
                    break
                for d in range(3):
                    if N == 3:
                        print(dic[a]+dic[b]+dic[c])
                        break
                    for e in range(3):
                        if N == 4:
                            print(dic[a]+dic[b]+dic[c]+dic[d])
                            break
                        for f in range(3):
                            if N == 5:
                                print(dic[a]+dic[b]+dic[c]+dic[d]+dic[e])
                                break
                            for g in range(3):
                                if N == 6:
                                    print(dic[a]+dic[b]+dic[c]+dic[d]+dic[e]+dic[f])
                                    break
                                for h in range(3):
                                    if N == 7:
                                        print(dic[a]+dic[b]+dic[c]+dic[d]+dic[e]+dic[f]+dic[g])
                                        break
                                    else:
                                        print(dic[a]+dic[b]+dic[c]+dic[d]+dic[e]+dic[f]+dic[g]+dic[h])

if __name__ == '__main__':
    main()