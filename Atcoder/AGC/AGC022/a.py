def main():
    S = input()
    alp = [chr(ord('a')+i) for i in range(26)]
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    elif len(S) < 26:
        tmp = sorted(list(set(S)-set(alp)))
        print(S+tmp[0])
    else:
        for i in range(len(S)):
            


if __name__ == '__main__':
    main()

abcdefghijklmnopqrstuvwzyx
abcdefghijklmnopqrstuvx