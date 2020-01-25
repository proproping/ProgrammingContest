def main():
    N = int(input())
    S = list(input())
    if len(S)%2 == 0:
        print(-1)
    else:
        tmp = len(S)//2+1
        ac = []
        for i in range(tmp):
            if i == 0:
                ac.append("b")
            elif i%3 == 1:
                ac.insert(0,"a")
                ac.append("c")
            elif i%3 == 2:
                ac.insert(0,"c")
                ac.append("a")
            else:
                ac.insert(0,"b")
                ac.append("b")
        if ac == S:
            print(tmp-1)
        else:
            print(-1)

if __name__ == '__main__':
    main()