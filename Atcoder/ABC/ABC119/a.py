def main():
    import datetime
    S = list(map(int,input().split("/")))
    tmp = datetime.date(S[0],S[1],S[2])
    if tmp <= datetime.date(2019,4,30):
        print("Heisei")
    else:
        print("TBD")

if __name__ == '__main__':
    main()