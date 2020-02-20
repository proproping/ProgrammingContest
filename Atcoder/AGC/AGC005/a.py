from collections import deque
def main():
    X = input()
    stack = deque([])
    for i in range(len(X)):
        if X[i] == "S":
            stack.append(X[i])
        else:
            if len(stack) != 0:
                tmp = stack.pop()
                if tmp == "T":
                    stack.append(tmp)
                    stack.append(X[i])
            else:
                stack.append(X[i])
    print(len(stack))
if __name__ == '__main__':
    main()