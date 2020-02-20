from collections import deque

def main():
    S = deque(list(input()))
    stack = deque([0])
    ans = 0
    while len(S) != 0:
        tmp = ""
        while len(S) != 0:
            before = stack.pop()
            tmp += S.popleft()
            if before != tmp:
                stack.append(tmp)
                ans += 1
                break
            else:
                stack.append(before)
    print(ans)

if __name__ == '__main__':
    main()