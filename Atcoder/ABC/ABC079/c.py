def main():
    from operator import sub,add
    tmp = input()
    A = int(tmp[0])
    B = int(tmp[1])
    C = int(tmp[2])
    D = int(tmp[3])
    dic = {0:sub,1:add}
    ansdic = {0:"-",1:"+"}
    ans = []
    for i in [0,1]:
        for j in [0,1]:
            for k in [0,1]:
                tmp1 = dic[i](A,B)
                tmp2 = dic[j](tmp1,C)
                tmp3 = dic[k](tmp2,D)
                if tmp3 == 7:
                    ans = [i,j,k]
                    break
    print(str(A)+ansdic[ans[0]]+str(B)+ansdic[ans[1]]+str(C)+ansdic[ans[2]]+str(D)+"=7")

if __name__ == '__main__':
    main()