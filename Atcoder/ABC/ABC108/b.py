def main():
    a,b,c,d = map(int,input().split())
    x = c-a
    y = d-b
    print(" ".join([str(c-y),str(d+x),str(a-y),str(b+x)]))

if __name__ == '__main__':
    main()