def main():
    x = int(input())
    account = 100
    ans = 0
    while account < x:
        account = int(account * 1.01)
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()