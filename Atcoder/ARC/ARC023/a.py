import datetime

def main():
    y = int(input())
    m = int(input())
    d = int(input())
    date1 = datetime.datetime(year=y,month=m,day=d,hour=1)
    date2 = datetime.datetime(year=2014,month=5,day=17,hour=1)
    print((date2-date1).days)

if __name__ == '__main__':
    main()