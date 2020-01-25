def main():
    S = input()
    d = S[0]
    c = 1
    runlength = []
    for i in range(1,len(S)):
        if d == S[i]:
            c += 1
        else:
            runlength.append([d,c])
            d = S[i]
            c = 1
        if i == len(S)-1:
            runlength.append([d,c])
    ans = [0]*len(S)
    ind = -1
    for rl in runlength:
        if rl[0] == "R":
            ind += rl[1]
            ans[ind] += rl[1] - rl[1]//2
            ans[ind+1] += rl[1]//2
        else:
            ans[ind] += rl[1]//2
            ans[ind+1] += rl[1] - rl[1]//2
            ind += rl[1]
    print(*ans)

if __name__ == '__main__':
    main()