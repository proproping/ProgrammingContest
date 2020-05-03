import copy

arrays = []
n,m,q = 0,0,0

def main():
    global n, m, q
    global arrays
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    ans = 0
    dfs([], 1)
    for array in arrays:
        tmp = 0
        for i in range(q):
            if array[abcd[i][1]-1] - array[abcd[i][0]-1] == abcd[i][2]:
                tmp += abcd[i][3]
        ans = max(ans, tmp)
    print(ans)

def dfs(stack, i):
    stack.append(i)
    if len(stack) == n:
        arrays.append(copy.deepcopy(stack))
        if i < m:
            stack.pop()
            dfs(copy.deepcopy(stack), i + 1)
        return
    dfs(copy.deepcopy(stack), i)
    if i < m:
        stack.pop()
        dfs(copy.deepcopy(stack), i + 1)

if __name__ == '__main__':
    main()