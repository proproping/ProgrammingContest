def main():
    time = sum([int(input()) for _ in range(4)])
    print("{}\n{}".format(time//60,time%60))

if __name__ == '__main__':
    main()