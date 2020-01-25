def main():
    s = input()
    k = int(input())
    tmp = []
    if len(list(s)) < k:
        print(0)
    else:
        for i in range(len(list(s))-k+1):
            tmp.append(s[i:i+k])
        print(len(list(set(tmp))))

if __name__ == '__main__':
    main()