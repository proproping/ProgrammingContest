def main():
    N = input()
    if N == N[::-1]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()