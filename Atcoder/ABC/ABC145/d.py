def main():
    import math
    X,Y = map(int,input().split())
    def comb(n,k,p):
        if n<0 or k<0 or n<k: return 0
        if n==0 or k==0: return 1
        a=math.factorial(n) %p
        b=math.factorial(k) %p
        c=math.factorial(n-k) %p
        return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
    def power_func(a,b,p):
        if b==0: return 1
        if b%2==0:
            d=power_func(a,b//2,p)
            return d*d %p
        if b%2==1:
            return (a*power_func(a,b-1,p ))%p
    if (X+Y)%3 != 0:
        print(0)
    else:
        n = int((2*Y-X)/3)
        m = int((2*X-Y)/3)
        nm = n+m
        k = min([n,m,nm-n,nm-m])
        print(comb(nm,k,10**9+7))

if __name__ == '__main__':
    main()