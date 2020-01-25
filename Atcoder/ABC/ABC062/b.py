def main():
    H,W = map(int,input().split())
    mat = [["#"]+list(input())+["#"] for i in range(H)]
    print("".join(["#"]*(W+2)))
    for i in range(len(mat)):
        print("".join(mat[i]))
    print("".join(["#"]*(W+2)))

if __name__ == '__main__':
    main()