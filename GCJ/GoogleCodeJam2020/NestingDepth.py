from itertools import groupby

def main():
    T = int(input())
    for i in range(T):
        S = input()
        gr = groupby(S)
        ans = ""
        for key, group in gr:
            tmp = list(group)
            if tmp[0] == "0":
                ans += "".join(tmp)
            else:
                ans += ("("+"".join(tmp)+")")

        print("Case #{}: {}".format(i+1,ans))

if __name__ == '__main__':
    main()