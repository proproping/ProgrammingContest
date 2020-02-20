def main():
    S = list(input())
    accum = [0]
    for i in range(1,len(S)):
        tmp = accum[i-1] + 1 if S[i-1] == "B" else accum[i-1]
        accum.append(tmp)
    ans = 0
    for i in range(len(S)):
        tmp = 0 if S[i] == "B" else accum[i]
        ans += tmp
    print(ans)

if __name__ == '__main__':
    main()