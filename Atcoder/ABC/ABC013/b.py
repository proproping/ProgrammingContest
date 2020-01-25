def main():
    a = int(input())
    b = int(input())
    tmp = [abs(a-b),abs(b-0)+abs(10-a),abs(a-0)+abs(10-b)]
    print(min(tmp))

if __name__ == '__main__':
    main()