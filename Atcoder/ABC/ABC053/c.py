import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import math
    x = int(input())
    if x <= 11:
        count = 0
        point = 0
        while True:
            point += 6
            count += 1
            if point >= x:
                break
            point += 5
            count += 1
            if point >= x:
                break
        print(count)
    else:
        count = math.ceil(x/11)*2
        if count%2 != 0:
            df = 6
        else:
            df = 5
        if count/2 * 11 - df >= x:
            count -= 1
        print(count)

if __name__ == '__main__':
    main()