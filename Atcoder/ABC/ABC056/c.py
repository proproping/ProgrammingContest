def main():
    X = int(input())
    t = 1
    while True:
        if (t*(t+1)/2) >= X:
            break
        else:
            t += 1
    print(t)

if __name__ == '__main__':
    main()