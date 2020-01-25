def main():
    x,y = map(str,input().split())
    tmp = {"1":1,"3":1,"5":1,"7":1,"8":1,"10":1,"12":1,"4":2,"6":2,"9":2,"11":2,"2":3}
    ans = []
    ans.append(tmp[x])
    ans.append(tmp[y])
    if ans[0] == ans[1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()