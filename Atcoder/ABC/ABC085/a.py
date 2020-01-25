def main():
    S = input()
    tmp = list(S)
    tmp[3] = "8"
    print("".join(tmp))

if __name__ == '__main__':
    main()