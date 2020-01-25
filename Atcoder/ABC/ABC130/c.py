def main():
    W,H,x,y = map(float,input().split())
    if y == (H/W)*x and y == H - (H/W)*x:
        tf = 1
    else:
        tf = 0
    print(" ".join([str(W*H/2),str(tf)]))

if __name__ == '__main__':
    main()