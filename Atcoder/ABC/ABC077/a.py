def main():
    C1 = list(input())
    C2 = list(input())
    tmp = []
    for i in range(3):
        tmp.append(C1[-i-1])
    if C2 == tmp:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()