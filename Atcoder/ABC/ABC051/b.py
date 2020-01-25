def main():
    K,S = map(int,input().split())
    count = 0
    for i in range(K+1):
        for j in range(K+1):
            X = i
            Y = j
            Z = S - i - j
            if 0 <= Z <= K:
                count += 1
    print(count)

if __name__ == '__main__':
    main()