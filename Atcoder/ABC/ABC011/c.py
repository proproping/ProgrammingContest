def main():
    N = int(input())
    NG = [int(input()) for _ in range(3)]
    count = 0
    for i in range(100):
        if count + 3 not in NG:
            count += 3
        elif count + 2 not in NG:
            count + 2
        elif count + 1 not in NG:
            count + 1
        else:
            break
    if N in NG:
        print("NO")
    elif count >= N:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()