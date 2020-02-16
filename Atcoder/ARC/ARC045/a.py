def main():
    S = list(input().split())
    ans = []
    for i in range(len(S)):
        if S[i] == "Left":
            ans.append("<")
        elif S[i] == "Right":
            ans.append(">")
        elif S[i] == "AtCoder":
            ans.append("A")
    print(*ans,sep=" ")


if __name__ == '__main__':
    main()