def main():
    import math
    H = int(input())
    ans = 0
    for i in range(int(math.log(H,2))+1):
        ans += 2**(i)
    print(ans)

if __name__ == '__main__':
    main()