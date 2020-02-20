from collections import Counter

def main():
    s = input()
    c = Counter(list(s))
    tg = "r"
    tmp = s
    for i in range(100):
        if tmp == tg*len(tmp):
            break
        tmp = ""
        for j in range(len(s)-i-1):
            if s[j] == tg or s[j+1] == tg:
                tmp += tg
            else:
                tmp += s[j]
    print(i)




if __name__ == '__main__':
    main()