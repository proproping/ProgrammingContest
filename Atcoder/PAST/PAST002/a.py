def main():
    s, t = map(to_int, input().split())
    print(abs(s-t))

def to_int(f):
    if f[0] == 'B':
        return - (int(f[1]) - 1)
    return int(f[0])

if __name__ == '__main__':
    main()