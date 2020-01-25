def main():
    A,B = map(int,input().split())
    tmp = []
    count = 0
    for i in range(A,B+1):
        tmp.append(i)
    for j in range(len(tmp)):
        flag = 1
        if len(str(tmp[j]))%2 == 0:
            for k in range(int(len(str(tmp[j]))/2)):
                if str(tmp[j])[k] != str(tmp[j])[-k-1]:
                    flag = 0
                    break
        else:
            for l in range(int(len(str(tmp[j]))//2)):
                if str(tmp[j])[l] != str(tmp[j])[-l-1]:
                    flag = 0
                    break
        if flag == 1:
            count += 1
    print(count)

if __name__ == '__main__':
    main()