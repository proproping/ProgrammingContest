def main():
    a,b = input().split()
    tmp = int(a+b)
    if tmp == int(tmp**(1/2))**2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()