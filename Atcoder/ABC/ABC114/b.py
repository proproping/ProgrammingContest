def main():
    S = input()
    tmp = []
    for i in range(len(S)-2):
        tmp.append(S[i:i+3])
    for j in range(len(S)-2):
        tmp[j] = abs(753-int(tmp[j]))
    print(min(tmp))

if __name__ == '__main__':
    main()