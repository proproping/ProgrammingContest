from collections import defaultdict

def main():
    N = int(input())
    s = defaultdict(int)
    ans = 0
    for i in range(N):
        a = "".join(sorted(input()))
        s[a] += 1
        if s[a] != 1:
            ans += (s[a]-1)
    print(ans)

if __name__ == '__main__':
    main()