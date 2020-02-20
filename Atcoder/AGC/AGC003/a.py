from collections import Counter
def main():
    S = list(input())
    c = Counter(S)
    if ((c["N"] == 0 and c["S"] == 0) or (c["N"] > 0 and c["S"] > 0)) and ((c["W"] == 0 and c["E"] == 0) or (c["W"] > 0 and c["E"] > 0)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()