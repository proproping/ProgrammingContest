def main():
    from itertools import combinations
    import numpy as np
    N,D = map(int,input().split())
    X = []
    for i in range(N):
        X.append(np.array(list(map(int,input().split()))))
    comb = list(combinations(list(range(N)),2))
    count = 0
    for i in range(len(comb)):
        dist = (sum(list(np.power(X[comb[i][0]]-X[comb[i][1]],2))))**(1/2)
        if int(dist) == dist:
            count += 1
    print(count)

if __name__ == '__main__':
    main()