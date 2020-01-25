def main():
    b = list(input())
    ans = list()
    for i in range(len(b)):
        if b[i] == "A":
            ans.append("T")
        elif b[i] == "T":
            ans.append("A")
        elif b[i] == "C":
            ans.append("G")
        else:
            ans.append("C")
    print("".join(ans))

if __name__ == '__main__':
    main()