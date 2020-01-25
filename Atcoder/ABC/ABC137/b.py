def main():
    import numpy as np
    k,x = map(int,input().split())
    ans = np.arange((x-k+1),(x+k))
    for i in range(len(ans)):
        print(ans[i], end = " ")

if __name__ == '__main__':
    main()