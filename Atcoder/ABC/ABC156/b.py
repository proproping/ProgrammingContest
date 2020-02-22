def to_k_base_num(n,k):
    bi = ""
    while n != 0:
        bi += str(n%abs(k))
        if k < 0:
            n = -(-n//k)
        else:
            n //= k
    return bi[::-1]

def main():
    N,K = map(int,input().split())
    print(len(str(to_k_base_num(N,K))))

if __name__ == '__main__':
    main()