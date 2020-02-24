def mod_comb(n,k,mod):
    result = 1
    for i in range(n-k+1,n+1):
        result *= i
        result %= mod
    for i in range(1,k+1):
        result *= pow(i,mod-2,mod)
        result %= mod
    return result

def main():
    n,a,b = map(int,input().split())
    mod = 10**9+7
    ans = pow(2,n,mod)-1
    ans = (ans - mod_comb(n,a,mod))%mod
    ans = (ans - mod_comb(n,b,mod))%mod
    print(ans)

if __name__ == '__main__':
    main()