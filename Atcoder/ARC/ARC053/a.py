def main():
    H,W = map(int,input().split())
    print((H-1)*W + (W-1)*H)

if __name__ == '__main__':
    main()