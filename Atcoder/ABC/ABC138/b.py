def main():
    import numpy as np
    n = int(input())
    a = np.array(list(map(int,input().split())))
    one = np.repeat(1,n)
    rec = one/a
    recsum = sum(rec)
    ans = 1/recsum
    print(ans)

if __name__ == '__main__':
    main()