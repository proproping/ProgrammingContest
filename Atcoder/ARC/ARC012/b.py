def main():
    N,va,vb,L = map(int,input().split())
    ans = L*(va/vb)**(-N)
    print('{:f}'.format(ans))

if __name__ == '__main__':
    main()