def main():
    D = int(input())
    ans = "Christmas"
    for i in range(25-D):
        ans += " Eve"
    print(ans)

if __name__ == '__main__':
    main()