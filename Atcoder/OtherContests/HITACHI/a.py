def main():
    S = input()
    lens = len(S)//2
    if S == "hi"*lens:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()