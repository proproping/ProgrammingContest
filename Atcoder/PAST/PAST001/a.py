def main():
    S = str(input())
    if len(S) != 3:
        print("error")
    else:
        try:
            print(int(S)*2)
        except ValueError as e:
            print("error")

if __name__ == '__main__':
    main()