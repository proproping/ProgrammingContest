def main():
    N = int(input())
    S = input()
    if N%2 != 0:
        print("No")
    else:
        if S[:int(N/2)] == S[int(N/2):]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()