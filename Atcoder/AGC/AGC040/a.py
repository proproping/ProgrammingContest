def main():
    from itertools import groupby
    r = p = 0
    for k,g in groupby(input()):
        l = sum([1 for _ in g])
        r += l*(l+1)//2
        if k == ">":
            r -= min(l,p)
        p = l
    print(r)

if __name__ == '__main__':
    main()