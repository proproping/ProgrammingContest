def main():
    import numpy as np
    D,N = map(int,input().split())
    tmp = list(range(1,100))
    tmp.append(101)
    tmp = np.array(tmp)
    tmp = tmp*(100**D)
    print(tmp[N-1])

if __name__ == '__main__':
    main()