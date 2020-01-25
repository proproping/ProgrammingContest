def main():
    dis1 = list(map(int,input().split()))
    dis2 = list(map(int,input().split()))
    if dis1[0] == dis2[0] or dis1[0] == dis2[1] or dis2[0] == dis1[1] or dis1[1] == dis2[1]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()