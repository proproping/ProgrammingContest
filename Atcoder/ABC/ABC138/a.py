def main():
    inputs = [input() for i in range(2)]
    a = int(inputs[0])
    s = str(inputs[1])
    if a >= 3200:
        print(s)
    else:
        print("red")

if __name__ == '__main__':
    main()