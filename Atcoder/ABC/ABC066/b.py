def main():
    S = list(input())
    if len(S)%2 != 0:
        del S[-1]
    else:
        del S[-1]
        del S[-1]
    while S[:int(len(S)/2)] != S[int(len(S)/2):]:
        del S[-1]
        del S[-1]
    print(len(S))

if __name__ == '__main__':
    main()