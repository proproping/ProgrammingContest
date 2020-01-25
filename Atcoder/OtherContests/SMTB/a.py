def main():
    one = list(map(int,input().split()))
    two = list(map(int,input().split()))
    if one[0] != two[0]:
        print("1")
    else:
        print("0")

if __name__ == '__main__':
    main()