from collections import Counter
def main():
    N = int(input())
    S = []
    for i in range(N):
        S += list(input())
    c = Counter(S)
    if c["R"] > c["B"]:
        print("TAKAHASHI")
    elif c["B"] > c["R"]:
        print("AOKI")
    else:
        print("DRAW")



if __name__ == '__main__':
    main()