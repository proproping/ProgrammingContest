def main():
    N = int(input())
    A = list(map(int,input().split()))
    mid = sum(A)/2
    length = 0
    i = 0
    while True:
        if length >= mid:
            length = min(abs(length-mid),abs(length-mid-A[i-1]))+mid
            break
        length += A[i]
        i += 1
    print(int(length-(sum(A)-length)))

if __name__ == '__main__':
    main()