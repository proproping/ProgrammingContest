def main():
    W = list(input())
    for i in range(len(W)):
        if W[i] in ["a","i","u","e","o"]:
            W[i] = ""
    print("".join(W))

if __name__ == '__main__':
    main()