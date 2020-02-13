from operator import itemgetter

def main():
    s = input()
    K = int(input())
    tmp = []
    for i in range(len(s)):
        tmp.append([s[i],i])
    tmp = sorted(tmp,key=itemgetter(0))
    print(tmp)

if __name__ == '__main__':
    main()