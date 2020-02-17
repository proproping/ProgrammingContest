import datetime

def main():
    y,m,d = map(int,input().split("/"))
    tmp = datetime.date(y,m,d)
    while True:
        y,m,d = tmp.year,tmp.month,tmp.day
        if y/m/d == int(y/m/d):
            break
        else:
            tmp += datetime.timedelta(days=1)
    print(datetime.datetime(y,m,d).strftime("%Y/%m/%d"))


if __name__ == '__main__':
    main()