def main():
    from collections import Counter
    n = int(input())
    ans = 0
    f,s = [],[]
    count = 0
    for i in map(int,input().split()):
        if count%2 == 0:
            f.append(i)
        else:
            s.append(i)
        count += 1
    c1,c2 = Counter(f),Counter(s)
    a,b = [],[]
    for i in c1.keys():
        a.append([i,c1[i]])
    for j in c2.keys():
        b.append([j,c2[j]])
    a = sorted(a,key=lambda x: x[1],reverse = True)
    b = sorted(b,key=lambda x: x[1],reverse = True)
    if a[0][0] == b[0][0]:
        if a[0][1] == b[0][1]:
            if len(a) == 1 and len(b) == 1:
                print(n-a[0][1])
            elif len(a) == 1 or len(b) == 1:
                if len(a) != 1:
                    print(n-a[1][1]-b[0][1])
                else:
                    print(n-a[0][1]-b[1][1])
            else:
                print(n-a[0][1]-max(a[1][1],b[1][1]))
        elif a[0][1] > b[0][1]:
            if len(b) == 1:
                print(n-a[0][1])
            else:
                print(n-a[0][1]-b[1][1])
        else:
            if len(a) == 1:
                print(n-b[0][1])
            else:
                print(n-a[1][1]-b[0][1])
    else:
        print(n-a[0][1]-b[0][1])

if __name__ == '__main__':
    main()