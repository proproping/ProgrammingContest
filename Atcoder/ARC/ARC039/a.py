def main():
    A,B = input().split()
    ans = -10**9
    for i in range(3):
        tmp = A
        s = "9"
        tmp = tmp[:i] + s + tmp[i+1:]
        ans = max(ans,int(tmp)-int(B))
    for i in range(3):
        tmp = B
        s = "0"
        if i == 0:
            s = "1"
        tmp = tmp[:i] + s + tmp[i+1:]
        ans = max(ans,int(A)-int(tmp))
    print(ans)

if __name__ == '__main__':
    main()