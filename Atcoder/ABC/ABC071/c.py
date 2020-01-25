def main():
    from collections import Counter
    N = int(input())
    A = list(map(int,input().split()))
    count = Counter(A)
    A = sorted(list(set(A)),reverse = True)
    a,b = 0,0
    for i in A:
        if a == 0:
            if count[i] >= 4:
                a,b = i,i
                break
            elif count[i] >= 2:
                a = i
        else:
            if count[i] >= 2:
                b = i
                break
    print(a*b)

if __name__ == '__main__':
    main()