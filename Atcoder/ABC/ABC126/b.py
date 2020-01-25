def main():
    S = input()
    tmp1 = int(S[:2])
    tmp2 = int(S[2:])
    if 0 < tmp1 <= 12 and 0 < tmp2 <= 12:
        print("AMBIGUOUS")
    elif (tmp1 == 0 or tmp1 > 12) and 0 < tmp2 <= 12:
        print("YYMM")
    elif 0 < tmp1 <= 12 and (tmp2 == 0 or tmp2 > 12):
        print("MMYY")
    else:
        print("NA")

if __name__ == '__main__':
    main()