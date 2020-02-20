import math
A,B,K,L = 0,0,0,0

def check(n):
    global A,B,K,L
    if (n//B)*L + (n-(n//B)*B)//A >= K:
        return True
    else:
        return False

def main():
    global A,B,K,L
    A,B,K,L = map(int,input().split())
    ub,lb = math.ceil(K/L)*B,1
    mid = math.ceil((ub+lb)/2)
    while ub-lb != 1:
        if check(mid):
            ub = mid
        else:
            lb = mid
        mid = math.ceil((ub+lb)/2)
    print(mid)


if __name__ == '__main__':
    main()