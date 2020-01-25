def main():
    A,B = map(int,input().split())
    S = input()
    ans = "Yes"
    flag1 = 0
    flag2 = 0
    if S[A] != "-":
        ans = "No"
    else:
        for i in range(A):
            if S[i] == "-":
                ans = "No"
                flag1 = 1
                break
        for j in range(A+1,A+B+1):
            if S[j] == "-":
                ans = "No"
                flag2 = 1
                break
    print(ans)

if __name__ == '__main__':
    main()