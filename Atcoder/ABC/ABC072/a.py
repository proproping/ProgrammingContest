def main():
    X,t = map(int,input().split())
    if X < t:
        print(0)
    else:
        print(X-t)

if __name__ == '__main__':
    main()