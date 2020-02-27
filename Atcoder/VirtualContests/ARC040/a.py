from collections import Counter

def main():
    N = int(input())
    S = ""
    for i in range(N):
        S += input()
    c = Counter(S)
    if c["R"] == c["B"]:
        print("DRAW")
    elif c["R"] > c["B"]:
        print("TAKAHASHI")
    else:
        print("AOKI")


if __name__ == '__main__':
    main()