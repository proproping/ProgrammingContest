def main():
    S = input()
    N = int(input())
    tmp = []
    for i in range(5):
        for j in range(5):
            tmp.append(S[i]+S[j])
    print(tmp[N-1])

if __name__ == '__main__':
    main()