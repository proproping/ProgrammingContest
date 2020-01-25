def main():
    m = int(input())
    if m < 100:
        print("00")
    elif 100 <= m <= 5000:
        ans = "0"+str(m//100)
        print(ans[-2:])
    elif 6000 <= m <= 30000:
        print(m//1000+50)
    elif 35000 <= m <= 70000:
        print(int((m//1000-30)/5+80))
    else:
        print("89")

if __name__ == '__main__':
    main()