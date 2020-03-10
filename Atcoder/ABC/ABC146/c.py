import math
A,B,X = 0,0,0

def check(n):
    if A*n + B*len(str(n)) <= X:
        return True
    else:
        return False

def main():
    global A,B,X
    A,B,X = map(int,input().split())
    ub,lb = 10**9+1,0
    mid = (ub + lb)//2
    while (ub - lb) > 1:
        if check(mid):
            lb = mid
        else:
            ub = mid
        mid = (ub + lb)//2
    print(mid)

if __name__ == '__main__':
    main()