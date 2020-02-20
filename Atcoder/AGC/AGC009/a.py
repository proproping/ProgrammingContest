import numpy as np

def main():
    N = int(input())
    A,B = np.array([0]*N),np.array([0]*N)
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    for i in range(N-1,-1,-1):
        tmp = (B[i] - A[i]%B[i])
        

if __name__ == '__main__':
    main()