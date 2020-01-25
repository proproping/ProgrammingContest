def main():
    a,b,c = map(int,input().split())
    tmp = sorted([a,b,c])
    print(tmp[0]+tmp[1])

if __name__ == '__main__':
    main()