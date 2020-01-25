def main():
    import math
    N = int(input())
    place = [list(map(int,input().split())) for _ in range(N)]
    print(place)
    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = math.sqrt((place[i][0]-place[j][0])**2+(place[i][1]-place[j][1])**2)
            if tmp > ans:
                ans = tmp
    print(ans)
if __name__ == '__main__':
    main()