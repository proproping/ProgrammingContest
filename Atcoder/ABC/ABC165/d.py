def main():
    a, b, n = map(int, input().split())
    ans = 0
    for i in range(n, -1, -1):
        if ans == 9:
            break
        print((int(a * i / b) - a * int(i / b)))
        ans = max(ans, (int(a * i / b) - a * int(i / b)))
    print("-----"+str(ans)+"----")
if __name__ == '__main__':
    main()