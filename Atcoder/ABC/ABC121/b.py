def main():
    import numpy as np
    N,M,C = map(int,input().split())
    B = np.array(list(map(int,input().split())))
    A = []
    for i in range(N):
        A.append(np.array(list(map(int,input().split()))))
    count = 0
    for i in range(N):
        if sum(list(A[i]*B))+C > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()