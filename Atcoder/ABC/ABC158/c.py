def main():
    A,B = map(int,input().split())
    for i in range(10000):
        if (int(i*0.08) == A) and (int(i*0.1) == B):
            break
    if i == 9999:
        print(-1)
    else:
        print(i)

if __name__ == '__main__':
    main()