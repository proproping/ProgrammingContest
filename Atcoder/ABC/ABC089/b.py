def main():
    N = int(input())
    S = input().split()
    ans = {3:"Three",4:"Four"}
    print(ans[len(set(S))])

if __name__ == '__main__':
    main()