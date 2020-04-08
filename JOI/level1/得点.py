def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max(sum(a),sum(b)))

if __name__ == '__main__':
    main()