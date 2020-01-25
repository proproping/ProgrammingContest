def main():
    S = list(input())
    ans = "AC"
    if S[0] != "A":
        ans = "WA"
    else:
        count = 0
        for i in S[2:-1]:
            if i == "C":
                count += 1
        if count != 1:
            ans = "WA"
        else:
            for i in S:
                if i not in ["A","C"] and str.islower(i) != True:
                    ans = "WA"
    print(ans)

if __name__ == '__main__':
    main()