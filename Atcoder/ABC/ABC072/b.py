def main():
    s = input()
    tmp = list(range(0,len(s),2))
    ans = []
    for i in tmp:
        ans.append(s[i])
    print("".join(ans))

if __name__ == '__main__':
    main()