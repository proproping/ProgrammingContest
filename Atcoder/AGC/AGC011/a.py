from collections import deque

def main():
    N,C,K = map(int,input().split())
    T = deque(sorted([int(input()) for _ in range(N)]))
    ans = 0
    while len(T) != 0:
        tmp = T.popleft()
        limit = tmp + K
        count = 1
        while count < C and len(T) != 0:
            tmp = T.popleft()
            if tmp > limit:
                T.appendleft(tmp)
                break
            else:
                count += 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()