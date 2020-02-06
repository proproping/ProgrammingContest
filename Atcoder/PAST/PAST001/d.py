def main():
    N = int(input())
    dic = dict(zip(list(range(1,N+1)),[0]*N))
    x,y = 0,0
    for i in range(N):
        dic[int(input())] += 1
    for i in range(1,N+1):
        if dic[i] == 0:
            y = i
        if dic[i] == 2:
            x = i
    if x == y:
        print("Correct")
    else:
        print(x,y)

if __name__ == '__main__':
    main()