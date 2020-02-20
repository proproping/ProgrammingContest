def main():
    A,B,C = list(map(int,input().split()))
    if A%2 == 0 or B%2 == 0 or C%2 == 0:
        print(0)
    else:
        print(min(A*C,A*B,C*B))

if __name__ == '__main__':
    main()