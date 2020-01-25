def main():
    W,a,b = map(int,input().split())
    if (b <= a+W and a <= b) or (a <= b+W and b <= a):
        print(0)
    elif a+W < b:
        print(b-(a+W))
    else:
        print(a-(b+W))

if __name__ == '__main__':
    main()