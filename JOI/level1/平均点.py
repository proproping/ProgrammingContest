def main():
    p = [int(input()) for i in range(5)]
    p = [p[i] if p[i] > 40 else 40 for i in range(5)]
    print(sum(p)//5)

if __name__ == '__main__':
    main()